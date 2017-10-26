# HtmlOutputer(object)的功能是：负责将爬取的数据写到文件中
import gc

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.txt', 'a', encoding='utf-8')
        for data in self.datas:
            # print(data)
            fout.write(''.join(data['node_XingMing']) + "#" + ''.join(data['node_ZuoPinShu']) + "#" +
                         ''.join(data['node_BeiYinLiang']) + "#" + ''.join(data['node_HZhiShu']) + "#" +
                         ''.join(data['node_GongZhiJiGou']) + "#" + ''.join(data['node_YanJiuZhuTi']) + "#" +
                         ''.join(data['node_YanJiuLingYu']) + "#" + ''.join(str(data['node_NumQiKan'])) + "#" +
                         ''.join(str(data['node_NumZhuanLi'])) + "#" + ''.join(str(data['node_NumHuiYi'])) + "#" +
                         ''.join(str(data['node_NumXueWei'])) + "#" + ''.join(str(data['node_NumZhuanZhu'])) + "#" +
                         ''.join(str(data['node_NumKeJi'])) + "#" + ''.join(str(data['node_Published2017'])) + "#" +
                         ''.join(str(data['node_Published2016'])) + "#" + ''.join(str(data['node_Published2015'])) + "#" +
                         ''.join(str(data['node_Published2014'])) + "#" + ''.join(str(data['node_Published2013'])) + "#" +
                         ''.join(data['node_PianShuPerJiGou']) +
                         '\n')
        fout.close()

    def reset(self):
        del self.datas
        gc.collect()
        self.datas = []
