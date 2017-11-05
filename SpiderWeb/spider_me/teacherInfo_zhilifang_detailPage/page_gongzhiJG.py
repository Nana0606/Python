import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.html_downloader as html_downloader4
from lxml import etree

class Spider_gongzhiJG(object):

    def __init__(self):
        self.downloader4 = html_downloader4.HtmlDownloader()

    def parse(self, html_cont, writerID):
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)

        # node_Published的元素依次代表：
        # 相关人物及相关人物所在的机构：node_Character

        node_GongzhiJG = {}
        # for i in range(1, 12):
        #     node_Related[i] = 0

        # 获取机构的页数
        pageNumDes = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']/"
                               "div[@class='m']/div[@class='search_op_bottom']/div[@class='pages']/span[@class='total']"
                               "/text()")
        pageNum = int(pageNumDes[0].replace("共", '').replace("页", ''))
        tempJG = []

        def addElemetTotemp(university):
            for toadd_index in range(0, len(university)):
                for added_index in range(0, len(tempJG)):
                    if university[toadd_index].find(tempJG[added_index]) != -1:   # 说明将要添加的机构名称不在已经添加的中
                        break
                    if added_index == (len(tempJG) - 1):
                        tempJG.append(university[toadd_index])

        university = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']"
                                "/div[@class='m']/div[@class='search_list type_writer']/dl/dt[1]/a/text()")
        tempJG.append(university[0])
        addElemetTotemp(university)
        if pageNum > 1:
            for number in range(2, pageNum + 1):
                # 每页对应的页面
                page_JG_url = "http://buidea.com:9001/writer/rw_jg.aspx?id=" + writerID +\
                              "&subid=&showname=&searchtype=&q=%7B%22page%22%3A%22" + str(number) \
                              + "%22%7D&&hfldSelectedIds=&"
                # 求出每一页的内容，需要和tempJG里的内容对比，看看是否是没有添加过的
                html_cont = self.downloader4.download(page_JG_url)
                data_page_JG = Spider_gongzhiJG().parse2(html_cont, writerID)
                addElemetTotemp(data_page_JG)
        node_tempJG = ""
        for school in tempJG:
            node_tempJG = node_tempJG + school + ";"
        # 提取出前5个相关人物及其对应的机构
        # node_Character = ""
        # if len(CharaName) < 5:
        #     for indexName in range(0, len(CharaName)):
        #         node_Character = node_Character + CharaName[indexName].replace(" ", '') + ":"\
        #                          + CharaJiGou[indexName].repalce("供职机构：", '') + ";"
        # else:
        #     for indexName in range(0, 5):
        #         node_Character = node_Character + CharaName[indexName].replace(" ", '') + ":" \
        #                          + CharaJiGou[indexName].replace("供职机构：", '') + ";"
        #
        list_wordParameters = ['node_gongzhiJG']
        # # for index in range(0, 1):
        # #     node_Related[list_wordParameters[index]] = node_Related[index]
        node_GongzhiJG[list_wordParameters[0]] = node_tempJG
        return node_GongzhiJG


    # 解析文件，返回一个数组
    def parse2(self, html_cont, writerID):
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)
        university = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']"
                                "/div[@class='m']/div[@class='search_list type_writer']/dl/dt/a/text()")
        return university



    def gongzhiJG(self, url_gongzhiJG, writerID):
        # 初始化
        html_cont = self.downloader4.download(url_gongzhiJG)
        data_gongzhiJG= Spider_gongzhiJG().parse(html_cont, writerID)
        return data_gongzhiJG



