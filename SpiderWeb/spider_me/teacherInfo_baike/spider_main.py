import GrabWeb.spider_me.teacherInfo_baike.html_downloader as html_downloader
import GrabWeb.spider_me.teacherInfo_baike.html_outputer as html_outputer
import GrabWeb.spider_me.teacherInfo_baike.html_parser as html_parser
import urllib.parse as parse

class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 抓取
    def craw(self, urls):
        count = 1
        for url in urls:
            try:
                print("craw", count, ": ", url)
                html_cont = self.downloader.download(url)
                new_data = self.parser.parse(url, html_cont)
                self.outputer.collect_data(new_data)
            except:
                print('craw failed')
            count = count + 1
        self.outputer.output_html()

if __name__ == "__main__":
    names = {"周傲英", "金澈清"}
    urls = set()
    for name in names:
        new_url = "https://baike.baidu.com/item/"+parse.quote(name)
        urls.add(new_url)
    obj_spider = SpiderMain()
    obj_spider.craw(urls)
