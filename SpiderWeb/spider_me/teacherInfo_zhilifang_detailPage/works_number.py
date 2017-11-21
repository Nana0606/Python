import re
from urllib import parse
import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree

uinfo = []

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

#解析网页信息获得科研人员的相关人员姓名，相关作品数，供职机构
def html_parse(uinfo, html_cont, ID, name, rel_teac, university, related_workers):
    if html_cont is None:
        print("html count:", html_cont)
        return
    try:
        tree = etree.HTML(html_cont)
        ZuoPinShu = tree.xpath("//div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='zps']/text()")
        print('作品数： ', ZuoPinShu)
        if len(ZuoPinShu) == 0:
            ZuoPinShu = ''
        else:
            ZuoPinShu = ZuoPinShu[0].replace("作品数：", '').replace(' ', '')
        uinfo.append(str(ID) + "," + str(name) + "," + str(rel_teac) + "," + str(university)
                 + "," + str(related_workers) + ',' + str(ZuoPinShu) )
        # print('uinfo: ', uinfo)
    except:
        print("error")

#把list里信息输出到txt文件中
def Output(uinfo):
    fout = open('related_teachers.txt', 'a', encoding='utf-8')
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
    # print(ID)
    return ID[0][22:37] #可能会有多个，提取第一个的ID

def main():

    queryFile = open("relatedteachers.txt", 'r', encoding='utf-8')
    # 读取文件中的每一行例如（4,冯建华,张兴,中国工程物理研究院激光聚变研究中心,7）搜索获得ID，最后通过该ID组成新的URL
    for query in queryFile:
        # 将输入文件中的每一行分割成导师姓名和学校
        splitRes = query.split(',')
        if len(splitRes) != 5:
            print(query, ' 格式不正确')
        else:
            global uinfo
            ID = query.split(',')[0].replace('\n', '').replace(' ', '')
            name = query.split(',')[1].replace('\n', '').replace(' ', '')
            rel_teac = query.split(',')[2].replace('\n', '').replace(' ', '')
            university = query.split(',')[3].replace('\n', '').replace(' ', '')
            related_workers = query.split(',')[4].replace('\n', '').replace(' ', '')
            print(ID + '#' + name + '#' + rel_teac + '#' + university + '#' + related_workers)
            # new_url = "https://baike.baidu.com/item/"+parse.quote(name)
            # 根据导师姓名和学校构造需要访问的url
            url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B"+parse.quote("\"")\
                      +"search"+parse.quote("\"")+"%3A"+parse.quote("\"")+parse.quote(rel_teac)+"%20"\
                      +parse.quote(university)+parse.quote("\"")+"%2C"+parse.quote("\"")+"sType"\
                      +parse.quote("\"")+"%3A"+parse.quote("\"")+"writer"+parse.quote("\"")+"%7D&"
            print("url is: ", url)
            html_cont = getHTMLText(url)
            html_parse(uinfo, html_cont, ID, name, rel_teac, university, related_workers)
            # print('uinfo: ', uinfo)
            if len(uinfo) % 100 == 0:
                Output(uinfo)
                uinfo = []
    Output(uinfo)

main()
