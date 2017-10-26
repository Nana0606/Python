from bs4 import BeautifulSoup
from lxml import etree
import urllib
import re

# HtmlParser(object)的功能是：负责解析html文本，取得页面的title，summary，页面中的urls

class HtmlParser2(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self.get_new_data(page_url, soup)
        return new_data

    def get_new_databeiyogn(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find("h1")
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        # summary_node = soup.find('div', class_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()
        return res_data

    def get_new_data(self, page_url, soup):
        res_data = {}
        # url
        # res_data['url'] = page_url
        div_node = soup.find('div', class_='search_list type_writer')
        res_data = div_node.get_text()
        return res_data

# 这个函数是正确的，在智立方的数据上，作者名称和学校信息都是来自网页，考虑到以后的匹配不一致，所以在HtmlParser函数中改为数据库中的字段
# 留用备份
class HtmlParserBeiFen(object):

    def parse(self, html_cont):
        res_data = {}
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)
        # print('tree: ', tree)
        #信息依次为：姓名、作品数、被引量、H指数、供职机构、研究主题
        node_XingMing = tree.xpath("//html//body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[2]/dl[1]/dt[@class='writer']/a/span/text()")
        ZuoPinShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='zps']/text()")
        # ZuoPinShu返回的是一个list
        node_ZuoPinShu = ZuoPinShu[0].split(u'：')[1]
        BeiYinLiang = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='bys']/text()")
        node_BeiYinLiang = BeiYinLiang[0].split(u'：')[1]
        HZhiShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='hzs']/text()")
        node_HZhiShu = HZhiShu[0].split(u'：')[1]
        # 供职机构存在一些问题：如“史作民 中国林业科学研究院” 搜索会得出很多span，这里仅将span的内容拼接，span之外的没有进行拼接
        #node_GongZhiJiGou = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='organ hide3 hide2']/span/text()")
        GongZhiJiGou1 = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='organ hide3 hide2']/span/text()")
        GongZhiJiGouTmp = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='organ hide3 hide2']/text()")
        GongZhiJiGou2 = GongZhiJiGouTmp[0].split(u'：')[1]
        if len(GongZhiJiGou1) != 0:
            node_GongZhiJiGou = GongZhiJiGou1
        else:
            node_GongZhiJiGou = GongZhiJiGou2
        # print('供职机构1：', GongZhiJiGou1, ' 供职机构2：', GongZhiJiGou2, ' 供职机构: ', node_GongZhiJiGou)
        YanJiuZhuTi = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='subject hide3 hide2']/text()")
        node_YanJiuZhuTi = YanJiuZhuTi[0].split(u'：')[1]
        print('node_XingMing: ', node_XingMing, "node_ZuoPinShu: ", node_ZuoPinShu, "node_BeiYinLiang: ", node_BeiYinLiang,
              "node_HZhiShu: ", node_HZhiShu, "node_GongZhiJiGou", node_GongZhiJiGou, " node_YanJiuZhuTi: ", node_YanJiuZhuTi)
        res_data['node_XingMing'] = node_XingMing
        res_data['node_ZuoPinShu'] = node_ZuoPinShu
        res_data['node_BeiYinLiang'] = node_BeiYinLiang
        res_data['node_HZhiShu'] = node_HZhiShu
        res_data['node_GongZhiJiGou'] = node_GongZhiJiGou
        res_data['node_YanJiuZhuTi'] = node_YanJiuZhuTi
        return res_data


class HtmlParser(object):

    def parse(self, html_cont, writer, school):
        res_data = {}
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)
        # print('tree: ', tree)
        #信息依次为：姓名、作品数、被引量、H指数、供职机构、研究主题
        node_XingMing = writer
        ZuoPinShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='zps']/text()")
        # ZuoPinShu返回的是一个list
        node_ZuoPinShu = ZuoPinShu[0].split(u'：')[1]
        BeiYinLiang = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='bys']/text()")
        node_BeiYinLiang = BeiYinLiang[0].split(u'：')[1]
        HZhiShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='hzs']/text()")
        node_HZhiShu = HZhiShu[0].split(u'：')[1]
        node_GongZhiJiGou = school
        YanJiuZhuTi = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='subject hide3 hide2']/text()")
        node_YanJiuZhuTi = YanJiuZhuTi[0].split(u'：')[1]
        print('node_XingMing: ', node_XingMing, "node_ZuoPinShu: ", node_ZuoPinShu, "node_BeiYinLiang: ", node_BeiYinLiang,
              "node_HZhiShu: ", node_HZhiShu, "node_GongZhiJiGou", node_GongZhiJiGou, " node_YanJiuZhuTi: ", node_YanJiuZhuTi)
        res_data['node_XingMing'] = node_XingMing
        res_data['node_ZuoPinShu'] = node_ZuoPinShu
        res_data['node_BeiYinLiang'] = node_BeiYinLiang
        res_data['node_HZhiShu'] = node_HZhiShu
        res_data['node_GongZhiJiGou'] = node_GongZhiJiGou
        res_data['node_YanJiuZhuTi'] = node_YanJiuZhuTi
        return res_data



