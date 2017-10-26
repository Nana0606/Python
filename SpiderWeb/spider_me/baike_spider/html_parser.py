from bs4 import BeautifulSoup
import urllib
import re

# HtmlParser(object)的功能是：负责解析html文本，取得页面的title，summary，页面中的urls

class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_url = self.get_new_url(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_url, new_data

    def get_new_url(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            new_url = "/item/"+urllib.parse.quote(link['href'].split("/")[2].split("?")[0])
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        # <h2>（计算机程序设计语言）</h2>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find("h1")
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data



