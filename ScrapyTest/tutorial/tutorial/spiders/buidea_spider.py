import scrapy
from urllib import parse
from tutorial.items import BuideaItem

class BuideaSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["buidea.com"]
    url_1 = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B" + parse.quote("\"") \
          + "search" + parse.quote("\"") + "%3A" + parse.quote("\"") + parse.quote("夏帆") + "%20" \
          + parse.quote("华东师范大学") + parse.quote("\"") + "%2C" + parse.quote("\"") + "sType" \
          + parse.quote("\"") + "%3A" + parse.quote("\"") + "writer" + parse.quote("\"") + "%7D&"
    url_2 = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B" + parse.quote("\"") \
            + "search" + parse.quote("\"") + "%3A" + parse.quote("\"") + parse.quote("高明") + "%20" \
            + parse.quote("华东师范大学") + parse.quote("\"") + "%2C" + parse.quote("\"") + "sType" \
            + parse.quote("\"") + "%3A" + parse.quote("\"") + "writer" + parse.quote("\"") + "%7D&"
    start_urls = [
        url_1,
        url_2
    ]

    def parse(self, response):
            item = BuideaItem()
            item['ZuopinShu'] = response.xpath("//div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='zps']/text()").extract()
            item['BeiyinLiang'] = response.xpath("//div[@class='search_list type_writer']/dl[1]/dd[@class='data hide3']/span[@class='bys']/text()").extract()
            yield item
