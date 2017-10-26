#!/usr/bin/python
# -*- coding: UTF-8 -*-
import GrabWeb.spider.url_manager as manager
import GrabWeb.spider.html_downloader as downloader
import GrabWeb.spider.html_outputer as outputer
import GrabWeb.spider.html_parser as parser
import urllib.parse as parse


class SpiderMain(object):
    # 初始各个对象， 其中UrlManager、HtmlDownloader、HtmlParser、HtmlOutputer四个对象需要之后创建
    def __init__(self):
        self.urls = manager.UrlManager()  # URL管理器
        self.downloader = downloader.HtmlDownloader()  # 下载器
        self.parser = parser.HtmlParser()  # 解析器
        self.outputer = outputer.HtmlOutputer()  # 输出器

    def craw(self, root_url):
        count = 1
        # 将root_url添加到url管理器
        self.urls.add_new_url(root_url)

        # 只要添加的url里有新的url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))

                # 这个页面说明找不到了
                if(new_url == 'http://baike.baidu.com/view/10812319.htm'):
                    print('是')
                else:
                    # 启动下载器，将获取到的url下载下来
                    html_cont = self.downloader.download(new_url)

                    # 调用解析器解析下载的这个页面
                    new_urls, new_data = self.parser.parse(new_url, html_cont)

                    # 将解析出的url添加到url管理器， 将数据添加到输出器里
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)

                    if count == 10:
                        break
                    count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()


if __name__ == "__main__":
    # 如果有中文，必须使用parse.quote将其转换成url格式
    root_url = "https://baike.baidu.com/item/" + parse.quote("你好")  # 这个URL根据实际情况的url进行修改
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
