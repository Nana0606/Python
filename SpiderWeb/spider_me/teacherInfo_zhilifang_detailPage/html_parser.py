import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.page_publishedWork as page_publishedWork
import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.page_relatedCharacter as page_relatedCharacter
import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.page_gongzhiJG as page_gongzhiJG
import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.page_ziZhu as page_ziZhu

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
        #信息依次为：姓名、作品数、被引量、H指数、供职机构、研究主题、研究领域、发表作品页（中英文文章都包括）的期刊文章数、专刊数、会议论文数、
        # 学位论文数、专著数、科技成果数、2017发表论文数、2016发表论文数、2015发表论文数、2014发表论文数、2013发表论文数、
        # 每个机构及对应发表论文数、每个传媒及对应发表论文数、相关人物、供职机构、前5个资助及对应论文篇数
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

        url_publishedWork = "http://buidea.com:9001/writer/rw_zp.aspx?id=" + writerID + "&subid=&showname=&searchtype="
        url_relatedCharacter = "http://buidea.com:9001/writer/rw_rw.aspx?id=" + writerID + "&subid=&showname=&searchtype="
        url_gongzhiJG = "http://buidea.com:9001/writer/rw_jg.aspx?id=" + writerID + "&subid=&showname=&searchtype="
        url_ziZhu = "http://buidea.com:9001/writer/rw_zz.aspx?id=" + writerID + "&subid=&showname=&searchtype="
        # print('detailPageUrl: ', detailPageUrl)
        data_publishedWork = page_publishedWork.Spider_publishedWork().publishWord(url_publishedWork)
        data_relatedCharacter = page_relatedCharacter.Spider_relatedCharacter().relatedCharacter(url_relatedCharacter)
        data_gongzhiJG = page_gongzhiJG.Spider_gongzhiJG().gongzhiJG(url_gongzhiJG, writerID)
        data_ziZhu = page_ziZhu.Spider_ziZhu().ziZhu(url_ziZhu)
        print("node_XingMing: ", node_XingMing, " data_ziZhu: ", data_ziZhu['node_ziZhu'])
        res_data['node_XingMing'] = node_XingMing
        res_data['node_ZuoPinShu'] = node_ZuoPinShu
        res_data['node_BeiYinLiang'] = node_BeiYinLiang
        res_data['node_HZhiShu'] = node_HZhiShu
        res_data['node_GongZhiJiGou'] = node_GongZhiJiGou
        res_data['node_YanJiuZhuTi'] = node_YanJiuZhuTi
        #result = dict(res_data, **data_publishedWork)
        result = {**res_data, **data_publishedWork, **data_relatedCharacter, **data_gongzhiJG, **data_ziZhu}
        return result
