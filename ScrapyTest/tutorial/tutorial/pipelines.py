# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log

class TutorialPipeline(object):
    def process_item(self, item, spider):
        file_name = 'items.txt'
        zuopinShu = item['ZuopinShu']
        beiyinLiang = item['BeiyinLiang']
        # print(item)
        # print("***************")
        # print(zuopinShu[0], " ", beiyinLiang[0])
        # print("testtets")
        # print(beiyinLiang)
        # print("***************")
        # print(zuopinShu[0])
        # for i, j in zip(zuopinShu, beiyinLiang):
        #     #f.write(item['ZuopinShu'] + ',' + item['BeiyinLiang'] + '\n')
        #     f.write(i + "," + j + '\n')
        # fp = open(file_name, 'w', encoding='utf-8')
        # fp.write(zuopinShu[0], ",", beiyinLiang[0])
        fout = open(file_name, 'a', encoding='utf-8')
        print(zuopinShu[0] + "," + beiyinLiang[0])
        fout.write(zuopinShu[0].replace('作品数：', '') + "," + beiyinLiang[0].replace('被引量：', '') + '\n')

        return item
