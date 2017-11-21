#智立方爬取某一老师的相关的科研人员信息
import re
import math
from urllib import parse
import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree

# 这个grade分别表示国家级、省级、市级、校级、其他, total_has_ziZhu是方便统计资助数目，用来计算没有参与资助的作品数
global total_has_ziZhu, grade_number
grade_number = [0, 0, 0, 0, 0]
total_has_ziZhu = 0

def isProvince(fund):
    city = ["上海市", "重庆市", "北京市", "深圳市", "省", "自治区"]
    for i in city:
        if i in fund:
            return "true"
    return "false"

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
    tree = etree.HTML(html)
    m = tree.xpath("//div[@class='search_count']/p/i/text()")
    # print('m为：', m)
    works_num = re.sub(r'\D', "", m[0])
    # num = m[0].replace('\r\n', '').replace(' ', '')  # 替换字符串的方式把换行符替换掉
    pages_num = math.ceil(float(works_num)/10.0)
    # print('记录数为：', works_num, '页数为：', pages_num)
    return works_num, pages_num

#解析网页信息获得科研人员的相关人员姓名，相关作品数，供职机构
def html_parse(ulist, html, name, university, works_Number):
    if html is None:
        print("html count:", html)
        return
    try:
        global total_has_ziZhu, grade_number
        tree = etree.HTML(html)
        funds = tree.xpath("//div[@class='search_list type_writer']/dl/dd[@class='hide2 hide3']/span[@class='fund']/text()") #所有该页面的资助
        # print(funds)
        zhuanLi = tree.xpath("//div[@class='search_list type_writer']/dl/dd[@class='hide3']/span/@class")
        for zL in zhuanLi:
            if zL == 'media zl':
                works_Number -= 1
        print(zhuanLi)
        total_has_ziZhu += len(funds)
        flag = 0
        for fund in funds:
            # fund.find("市") != -1表示fund中包含“市”
            if fund.find("国家") != -1 or fund.find("教育部") != -1 or fund.find("中国") != -1 or fund.find("国防") != -1 \
                    or fund.find("科技部") != -1 or fund.find("中央") != -1 or fund.find("国家级") != -1:
                grade_number[0] += 1
                # print("国家级： ", fund)
                flag = 1
            if isProvince(fund) == "true" or fund.find("省") != -1:
                grade_number[1] += 1
                # print("省级： ", fund)
                flag = 1
            if fund.find("市") != -1 and fund.find("上海市") == -1 and fund.find("重庆市") == -1 and fund.find("北京市") == -1 and fund.find("深圳市") == -1:
                grade_number[2] += 1
                print("市级： ", fund)
                flag = 1
            if fund.find("大学") != -1 or fund.find("学院") != -1:
                grade_number[3] += 1
                # print("校级： ", fund)
                flag = 1
        if flag == 0:
            grade_number[4] += 1
            # print("其他： ", fund)
        # #把该页的相关信息合并成一个字符串放入ulist
        # for i in range(len(re_people)):
        #     #这边这个判断是为了排除有一些人的相关作品是0
        #     if len(re_work[i])>= 6:
        #         ulist.append(str(name)+","+str(re_people[i])+","+str(agency[i][5:])+","+str(re_work[i][6:]))
        #     else:
        #         ulist.append(str(name) + "," + str(re_people[i]) + "," + str(agency[i][5:]) + "," + str(re_work[i]))
        return works_Number
    except:
        print("error")

#把list里信息输出到txt文件中
def Output(uinfo):
    fout = open('teachers_fund.txt', 'a', encoding='utf-8')
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
    return ID[0][22:37] #可能会有多个，提取第一个的ID

def main():

    queryFile = open("teacherInfo_2.txt", 'r', encoding='utf-8')
    # 读取文件中的每一行例如（冯建华 清华大学）搜索获得ID，最后通过该ID组成新的URL
    for query in queryFile:
        # 将输入文件中的每一行分割成导师姓名和学校
        global total_has_ziZhu, grade_number
        splitRes = query.split(',')
        if len(splitRes) != 2:
            print(query, ' 格式不正确')
        else:
            uinfo = []
            name = query.split(',')[0]
            # print(name)
            university = query.split(',')[1].replace('\n', '')
            # print(university)
            # new_url = "https://baike.baidu.com/item/"+parse.quote(name)
            # 根据导师姓名和学校构造需要访问的url

            new_url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B"+parse.quote("\"")\
                      +"search"+parse.quote("\"")+"%3A"+parse.quote("\"")+parse.quote(name)+"%20"\
                      +parse.quote(university)+parse.quote("\"")+"%2C"+parse.quote("\"")+"sType"\
                      +parse.quote("\"")+"%3A"+parse.quote("\"")+"writer"+parse.quote("\"")+"%7D&"
            # print(new_url)
            #通过该url获得对应的ID
            UrlID=getID(new_url)
            # print(UrlID)
            #构造这个人需要访问的URL
            url = "http://buidea.com:9001/writer/rw_zp.aspx?id=" + str(UrlID) + "&subid=&showname=&searchtype="
            print('url testing: ', url)
            html = getHTMLText(url)
            works_num, pages_num = getpage(html)
            works_Number = int(works_num)
            pages_Number = int(pages_num)
            if pages_Number != 0:
                for i in range(1, pages_Number + 1):
                    url = "http://buidea.com:9001/writer/rw_zp.aspx?id=" + str(UrlID) + "&subid=&showname=&searchtype=&q=%7B%22page%22%3A%22" + str(i) + "%22%7D&&hfldSelectedIds=&"
                    print("相关页面url：" + url)
                    new_html = getHTMLText(url)
                    works_Number = html_parse(uinfo, new_html, name, university, works_Number)
            uinfo.append(str(name) + "," + str(university) + "," + str(grade_number[0]) + "," + str(grade_number[1])
                         + "," + str(grade_number[2]) + "," + str(grade_number[3]) + "," + str(grade_number[4])
                         + "," + str(works_Number - total_has_ziZhu))
            print('uinfo: ', uinfo)
            Output(uinfo)
            total_has_ziZhu = 0
            grade_number = [0, 0, 0, 0, 0]

main()
