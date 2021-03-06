import GrabWeb.spider_me.teacherInfo_zhilifang_detailPage.html_downloader as html_downloader2
from lxml import etree

class Spider_publishedWork(object):

    def __init__(self):
        self.downloader2 = html_downloader2.HtmlDownloader()

    def parse(self, html_cont):
        data_publishedWork = {}
        if html_cont is None:
            print("html count:", html_cont)
            return
        tree = etree.HTML(html_cont)

        # node_Published的元素依次代表：
        # 期刊文章数：node_NumQiKan、专刊数：node_NumZhuanLi、会议论文数：node_NumHuiYi、学位论文数：node_NumXueWei、
        # 专著数：node_NumZhuanZhu、科技成果数：node_NumKeJi、
        # 2017发表文章数：node_Published2017、2016发表文章数：node_Published2016、2015发表文章数：node_Published2015、
        # 2014发表文章数：node_Published2014、2013发表文章数：node_Published2013
        # node_PianShuPerJiGou：每个作者对应的前5个机构及篇数
        # node_PianShuPerChuanMei: 每个作者对应的前5个传媒及篇数

        node_Published = {}
        node_Published[0] = " "
        for i in range(1, 12):
            node_Published[i] = 0
        for i in range(12, 14):
            node_Published[i] = " "

        # 作者的研究领域字段获取
        YanJiuLingYu = tree.xpath("/html/body/div[@class='body object_writer']/div[@class='main']/div[@class='summary']/p[4]/text()")
        node_Published[0] = YanJiuLingYu[0].split(u'：')[1]

        WenXianShuMu = tree.xpath("//*[@id='titletypecluster']/div/ul/li/tt/text()")
        WenXianMingCheng = tree.xpath("//*[@id='titletypecluster']/div/ul/li/span/text()")

        # 判断是否属于给定的类型，若属于则附上相应的值，否则值为0
        indexWenZhang = 0
        for type in WenXianMingCheng:
            if type.find("期刊文章") != (-1):
                node_Published[1] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            elif type.find("专利") != (-1):
                node_Published[2] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            elif type.find("会议论文") != (-1):
                node_Published[3] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            elif type.find("学位论文") != (-1):
                node_Published[4] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            elif type.find("专著") != (-1):
                node_Published[5] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            elif type.find("科技成果") != (-1):
                node_Published[6] = WenXianShuMu[indexWenZhang].replace("篇", '').replace(',', '')
            else:
                pass
            indexWenZhang = indexWenZhang + 1
        # for each in WenXianLeiXing:
        #     print(each, "  ")
        PianShu = tree.xpath("//*[@id='yearcluster']/div/ul/li/tt/text()")
        NianFen = tree.xpath("//*[@id='yearcluster']/div/ul/li/span/text()")
        # 判断是否属于给定的类型，若属于则附上相应的值，否则值为0
        indexYear = 0
        for year in NianFen:
            if year < "2013":
                break
            else:
                if year == "2017":
                    node_Published[7] = PianShu[indexYear].replace("篇", '').replace(',', '')
                elif year == "2016":
                    node_Published[8] = PianShu[indexYear].replace("篇", '').replace(',', '')
                elif year == "2015":
                    node_Published[9] = PianShu[indexYear].replace("篇", '').replace(',', '')
                elif year == "2014":
                    node_Published[10] = PianShu[indexYear].replace("篇", '').replace(',', '')
                elif year == "2013":
                    node_Published[11] = PianShu[indexYear].replace("篇", '').replace(',', '')
                else:
                    pass
            indexYear = indexYear + 1

        # 获取发表作品页面每个机构对应的篇数
        ShuMuJG = tree.xpath("//*[@id='organcluster']/div/ul/li/tt/text()")
        JiGou = tree.xpath("//*[@id='organcluster']/div/ul/li/@title")
        node_PianShuPerJiGou = ""
        if len(ShuMuJG) < 5:
            for timeJG in range(0, len(ShuMuJG)):
                node_PianShuPerJiGou = node_PianShuPerJiGou + JiGou[timeJG].replace(" ", '') + ":" + ShuMuJG[timeJG] + ";"
        else:
            for timeJG in range(0, 5):
                node_PianShuPerJiGou = node_PianShuPerJiGou + JiGou[timeJG].replace(" ", '') + ":" + ShuMuJG[timeJG] + ";"

        # 获取发表作品页面每个传媒对应的篇数
        ShuMuCM = tree.xpath("//*[@id='mediacluster']/div/ul/li/tt/text()")
        ChuanMei = tree.xpath("//*[@id='mediacluster']/div/ul/li/@title")
        node_PianShuPerChuanMei = ""
        if len(ShuMuCM) < 5:
            for timeCM in range(0, len(ShuMuCM)):
                node_PianShuPerChuanMei = node_PianShuPerChuanMei + ChuanMei[timeCM].replace(" ", '') + ":" + ShuMuCM[timeCM] + ";"
        else:
            for timeCM in range(0, 5):
                node_PianShuPerChuanMei = node_PianShuPerChuanMei + ChuanMei[timeCM].replace(" ", '') + ":" + ShuMuCM[timeCM] + ";"

        list_wordParameters = ['node_YanJiuLingYu', 'node_NumQiKan', 'node_NumZhuanLi', 'node_NumHuiYi',
                               'node_NumXueWei', 'node_NumZhuanZhu', 'node_NumKeJi', 'node_Published2017',
                               'node_Published2016', 'node_Published2015', 'node_Published2014', 'node_Published2013',
                               'node_PianShuPerJiGou', 'node_PianShuPerChuanMei']
        for index in range(0, 12):
            data_publishedWork[list_wordParameters[index]] = node_Published[index]
        data_publishedWork[list_wordParameters[12]] = node_PianShuPerJiGou
        data_publishedWork[list_wordParameters[13]] = node_PianShuPerChuanMei
        return data_publishedWork

    def publishWord(self, url_publishedWord):
        # 初始化
        html_cont = self.downloader2.download(url_publishedWord)
        data_publishedWork= Spider_publishedWork().parse(html_cont)
        return data_publishedWork

