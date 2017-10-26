from bs4 import BeautifulSoup
import urllib
import re

# HtmlParser(object)的功能是：负责解析html文本，取得页面的title，summary，页面中的urls

class HtmlParser(object):

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
        div_node = soup.find('div', class_='main-content')
        res_data = div_node.get_text()
        return res_data




