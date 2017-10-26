import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.page_publishedWork as page_publishedWork
from bs4 import BeautifulSoup
from lxml import etree

# HtmlParser(object)的功能是：负责解析html文本，取得页面各元素
class HtmlParser(object):

    def parse(self, html_cont, writer, school):
        res_data = {}
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)
        # print('tree: ', tree)
        #信息依次为：姓名、作品数、被引量、H指数、供职机构、研究主题、研究领域、发表作品页（中英文文章都包括）的期刊文章、专刊、会议论文、
        # 学位论文、专著、科技成果、2017发表论文数、2016发表论文数、2015发表论文数、2014发表论文数、2013发表论文数
        node_XingMing = writer
        ZuoPinShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='zps']/text()")
        # ZuoPinShu返回的是一个list
        node_ZuoPinShu = ZuoPinShu[0].split(u'：')[1].replace(",", "")
        BeiYinLiang = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='bys']/text()")
        node_BeiYinLiang = BeiYinLiang[0].split(u'：')[1].replace(",", "")
        HZhiShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='hzs']/text()")
        node_HZhiShu = HZhiShu[0].split(u'：')[1].replace(",", "")
        node_GongZhiJiGou = school
        YanJiuZhuTi = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl[1]//dd[@class='subject hide3 hide2']/text()")
        node_YanJiuZhuTi = YanJiuZhuTi[0].split(u'：')[1].replace(" ", ";")

        node_detailPageUrl = tree.xpath(
            "//html//body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[2]/dl[1]/dt[@class='writer']/a/@href")
        # print("node_detailPageUrl: ", node_detailPageUrl[0])
        detailPageUrlTmp = node_detailPageUrl[0].replace("/writer/rw_zp.aspx?id=", "")
        writerID = detailPageUrlTmp.replace("&subid=&showname=&searchtype=", "")
        detailPageUrl = "http://buidea.com:9001/writer/rw_zp.aspx?id=" + writerID + "&subid=&showname=&searchtype="
        # print('detailPageUrl: ', detailPageUrl)
        data_publishedWork = page_publishedWork.Spider_detailPage().detailInfo(detailPageUrl)

        print(' node_XingMing: ', node_XingMing, " node_ZuoPinShu: ", node_ZuoPinShu, " node_BeiYinLiang: ", node_BeiYinLiang,
              " node_HZhiShu: ", node_HZhiShu, " node_GongZhiJiGou", node_GongZhiJiGou, " node_YanJiuZhuTi: ", node_YanJiuZhuTi,
              " node_PianShuPerJiGou: ", data_publishedWork['node_PianShuPerJiGou']
              )
        res_data['node_XingMing'] = node_XingMing
        res_data['node_ZuoPinShu'] = node_ZuoPinShu
        res_data['node_BeiYinLiang'] = node_BeiYinLiang
        res_data['node_HZhiShu'] = node_HZhiShu
        res_data['node_GongZhiJiGou'] = node_GongZhiJiGou
        res_data['node_YanJiuZhuTi'] = node_YanJiuZhuTi
        result = dict(res_data, **data_publishedWork)
        return result
