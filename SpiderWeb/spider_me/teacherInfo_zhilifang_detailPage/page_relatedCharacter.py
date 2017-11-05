import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.html_downloader as html_downloader3
from lxml import etree

class Spider_relatedCharacter(object):

    def __init__(self):
        self.downloader3 = html_downloader3.HtmlDownloader()

    def parse(self, html_cont):
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)

        # node_Related的元素依次代表：
        # 相关人物及相关人物所在的机构：node_Character、

        node_Related = {}
        # for i in range(1, 12):
        #     node_Related[i] = 0

        # 获取相关人物及相关人物所在的机构
        CharaName = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']/"
                               "div[@class='m']/div[@class='search_list type_writer']/dl/dt[@class='writer']"
                               "/a/text()")
        CharaJiGou = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']/"
                               "div[@class='m']/div[@class='search_list type_writer']/dl"
                                "/dd[@class='organ hide3 hide2']/text()")
        # 提取出前5个相关人物及其对应的机构
        node_Character = ""
        if len(CharaName) < 5:
            for indexName in range(0, len(CharaName)):
                node_Character = node_Character + CharaName[indexName].replace(" ", '') + ":"\
                                 + CharaJiGou[indexName].replace("供职机构：", '') + ";"
        else:
            for indexName in range(0, 5):
                node_Character = node_Character + CharaName[indexName].replace(" ", '') + ":" \
                                 + CharaJiGou[indexName].replace("供职机构：", '') + ";"
        list_wordParameters = ['node_Character']
        # for index in range(0, 1):
        #     node_Related[list_wordParameters[index]] = node_Related[index]
        node_Related[list_wordParameters[0]] = node_Character
        return node_Related

    def relatedCharacter(self, url_relatedCharacter):
        # 初始化
        html_cont = self.downloader3.download(url_relatedCharacter)
        data_relatedCharacter= Spider_relatedCharacter().parse(html_cont)
        return data_relatedCharacter

