import GrabWeb.spider_me.teacherInfo_zhilifang_withParametersFromDB.html_downloader as html_downloader
import GrabWeb.spider_me.teacherInfo_zhilifang_withParametersFromDB.html_outputer as html_outputer
import GrabWeb.spider_me.teacherInfo_zhilifang_withParametersFromDB.html_parser as html_parser
import urllib.parse as parse
import gc

# 本代码抓取的页面是作者查询页面中的一部分信息
# 如页面：http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B%22search%22%3A%22%E5%91%A8%E5%82%B2%E8%8B%B1%20%E5%8D%8E%E4%B8%9C%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6%22%2C%22sType%22%3A%22writer%22%7D&


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
            # 需要姓名和学校来自数据库，因此添加内容如下：
            urlTmp1 = url.replace("http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B%22search%22%3A%22", "")
            urlTmp2 = urlTmp1.replace("%22%2C%22sType%22%3A%22writer%22%7D&", "")
            info = parse.unquote(urlTmp2, encoding='utf-8')
            writer = info.split(' ')[0]
            school = info.split(' ')[1].replace('\n', '')
            try:
                print("craw", count, ": ", url)
                html_cont = self.downloader.download(url)
                # print('test for html_cont')

                new_data = self.parser.parse(html_cont, writer, school)
                # print('new_data: ', new_data)
                self.outputer.collect_data(new_data)
            except:
                print("craw failed： count = ", count)
            if count % 3000 == 0:
                self.outputer.output_html()
                print("前", count, "行已输出到output.txt文件")
                # 将之前已经添加到缓存的内容清空
                self.outputer.reset()
            count = count + 1
            del urlTmp1, urlTmp2, info, writer, school
            gc.collect()
        self.outputer.output_html()
        print('最后一波写入输出文件')
        self.outputer.reset()
        print(count - 1)

if __name__ == "__main__":
    queryFile = open("in.txt", 'r', encoding='utf-8')
    urls = set()
    for query in queryFile:
        splitRes = query.split('\t')
        if len(splitRes) != 2:
            print(query, ' 格式不正确')
        else:
            name = query.split('\t')[0]
            university = query.split('\t')[1]
            # print(name, "***分界线***", university)
            # new_url = "https://baike.baidu.com/item/"+parse.quote(name)
            new_url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B"+parse.quote("\"")\
                      +"search"+parse.quote("\"")+"%3A"+parse.quote("\"")+parse.quote(name)+"%20"\
                      +parse.quote(university)+parse.quote("\"")+"%2C"+parse.quote("\"")+"sType"\
                      +parse.quote("\"")+"%3A"+parse.quote("\"")+"writer"+parse.quote("\"")+"%7D&"
            urls.add(new_url)
    #print(urls)
    obj_spider = SpiderMain()
    obj_spider.craw(urls)
    del urls
    gc.collect()
