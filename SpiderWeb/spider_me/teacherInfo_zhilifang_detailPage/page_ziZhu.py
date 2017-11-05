import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.html_downloader as html_downloader5
from lxml import etree

class Spider_ziZhu(object):

    def __init__(self):
        self.downloader5 = html_downloader5.HtmlDownloader()

    def parse(self, html_cont):
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)
        # node_Related的元素依次代表：
        # 相关人物及相关人物所在的机构：node_Character、
        node_ziZhu = {}
        # for i in range(1, 12):
        #     node_Related[i] = 0

        # 获取相关资助及其个数
        name_ziZhu = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']/"
                               "div[@class='m']/div[@class='search_list type_writer']/dl/dt[@class='fund ']"
                               "/a/text()")
        number_ziZhu = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='search']/"
                               "div[@class='m']/div[@class='search_list type_writer']/dl"
                                "/dt[@class='fund ']/span[@class='relative']/a/text()")
        # 提取出前5个相关人物及其对应的机构
        ziZhu= ""
        ##注意：存在一点小的bug：如果一个资助写成2行，会出现一些问题
        if len(name_ziZhu) < 5:
            for indexName in range(0, len(name_ziZhu)):
                ziZhu = ziZhu + name_ziZhu[indexName].replace(" ", '') + ":"\
                                 + number_ziZhu[indexName].replace("相关作品数：", '') + ";"
        else:
            for indexName in range(0, 5):
                ziZhu = ziZhu + name_ziZhu[indexName].replace(" ", '') + ":" \
                                 + number_ziZhu[indexName].replace("相关作品数：", '') + ";"
        list_wordParameters = ['node_ziZhu']
        # for index in range(0, 1):
        #     node_Related[list_wordParameters[index]] = node_Related[index]
        node_ziZhu[list_wordParameters[0]] = ziZhu
        return node_ziZhu

    def ziZhu(self, url_ziZhu):
        # 初始化
        html_cont = self.downloader5.download(url_ziZhu)
        data_ziZhu= Spider_ziZhu().parse(html_cont)
        return data_ziZhu

