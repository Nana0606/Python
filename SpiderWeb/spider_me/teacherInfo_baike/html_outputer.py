# HtmlOutputer(object)的功能是：负责将爬取的数据写到文件中

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.txt', 'w', encoding='utf-8')
        for data in self.datas:
              fout.write(data+'\n')
        fout.close()
