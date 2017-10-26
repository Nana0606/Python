import GrabWeb.spider_me.baike_spider.html_downloader as html_downloader
import GrabWeb.spider_me.baike_spider.html_outputer as html_outputer
import GrabWeb.spider_me.baike_spider.html_parser as html_parser
import GrabWeb.spider_me.baike_spider.url__manager as url_manager
import urllib.parse as parse

class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 抓取
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/"+parse.quote("周傲英")
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
