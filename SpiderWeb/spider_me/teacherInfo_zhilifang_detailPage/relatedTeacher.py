#智立方爬取某一老师的相关的科研人员信息
import re
from urllib import parse
import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree

# 该函数用Requests库将网页爬取下来
def getHTMLText(url):
    # 爬取网页的通用代码框架
    try:
        kv = {'user-agent': 'Mozilla/5.0'}#该参数是设置用浏览器的形式访问网站
        r = requests.get(url, headers=kv, timeout=30)#爬取网页生成response对象
        r.raise_for_status()
        r.encoding = r.apparent_encoding#判断是否爬取成功
        return r.text         #返回爬虫的文本内容
    except:
        return ""
#解析网页并获得页码信息
#因为需要爬取多页信息，所以先获得一共多少页
def getpage(html):
    soup = BeautifulSoup(html, "html.parser")#用BeatifulSoup库来解析网页
    m = soup.find_all('span', class_="total")#用find_all方法找到包含总页数的那个标签
    if len(m)!= 0:
        print(m[0])
        num = re.sub(r'\D', "", str(m[0]))#用正则的方式把非数字的部分删除掉
        print(num)
        return num
    else:
        return 0

#解析网页信息获得科研人员的相关人员姓名，相关作品数，供职机构
def html_parse(ulist, html,name):
    if html is None:
        print("html count:", html)
        return
    try:
        tree = etree.HTML(html)
        re_people = tree.xpath("//div[@class='search_list type_writer']/dl/dt[@class='writer']/a/text()") #相关人员姓名
        agency = tree.xpath("//div[@class='search_list type_writer']/dl/dd[@class='organ hide3 hide2']/text()") #供职机构
        re_work = tree.xpath("//div[@class='search_list type_writer']/dl/dt[@class='writer']/span[@class='relative']/a/text()") #相关作品数
        print(re_people)
        #把该页的相关信息合并成一个字符串放入ulist
        for i in range(len(re_people)):
            #这边这个判断是为了排除有一些人的相关作品是0
            if len(re_work[i])>= 6:
                ulist.append(str(name)+","+str(re_people[i])+","+str(agency[i][5:])+","+str(re_work[i][6:]))
            else:
                ulist.append(str(name) + "," + str(re_people[i]) + "," + str(agency[i][5:]) + "," + str(re_work[i]))
    except:
        print("error")
#把list里信息输出到txt文件中
def Output(uinfo):
    fout = open('relatedTeacher.txt', 'a', encoding='utf-8')
    for data in uinfo:
        fout.write(data+'\n')
    fout.close()
#解析网页获得对应科研人员的url中的ID
#通过定位该ID可以找到该科研人员各个相关页面
def getID(newurl):
    if newurl is None:
        print("html count:", newurl)
        return
    html = getHTMLText(newurl)
    tree = etree.HTML(html) #用lxml来解析网页
    ID = tree.xpath("//div[@class='search_list type_writer']/dl/dt[@class='writer']/a/@href")
    print(ID)
    return ID[0][22:37]#可能会有多个，提取第一个的ID

def main():

    queryFile = open("in.txt", 'r', encoding='utf-8')
    # 读取文件中的每一行例如（冯建华 清华大学）搜索获得ID，最后通过该ID组成新的URL
    for query in queryFile:
        # 将输入文件中的每一行分割成导师姓名和学校
        splitRes = query.split(',')
        if len(splitRes) != 2:
            print(query, ' 格式不正确')
        else:
            uinfo = []
            name = query.split(',')[0]
            print(name)
            university = query.split(',')[1]
            print(university)
            # new_url = "https://baike.baidu.com/item/"+parse.quote(name)
            # 根据导师姓名和学校构造需要访问的url

            new_url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B" + parse.quote("\"")\
                      + "search" + parse.quote("\"") + "%3A" + parse.quote("\"") + parse.quote(name) + "%20"\
                      + parse.quote(university) + parse.quote("\"") + "%2C" + parse.quote("\"") + "sType"\
                      + parse.quote("\"") + "%3A" + parse.quote("\"") + "writer" + parse.quote("\"") + "%7D&"
            print(new_url)
            #通过该url获得对应的ID
            UrlID=getID(new_url)
            print(UrlID)
            #构造这个人需要访问的URL
            url = "http://buidea.com:9001/writer/rw_rw.aspx?id="+str(UrlID)+"&subid=&showname=&searchtype=&q=%7B%22page%22%3A%221%22%7D&&hfldSelectedIds=&"
            html = getHTMLText(url)
            n = int(getpage(html))
            if n != 0:
                for i in range(1, n + 1):
                    url = "http://buidea.com:9001/writer/rw_rw.aspx?id="+str(UrlID)+"&subid=&showname=&searchtype=&q=%7B%22page%22%3A%22" + str(i) + "%22%7D&&hfldSelectedIds=&"
                    new_html = getHTMLText(url)
                    html_parse(uinfo, new_html, name)
            Output(uinfo)

main()
