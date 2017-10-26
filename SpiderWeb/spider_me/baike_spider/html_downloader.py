import urllib.request

#  HtmlDownloader(object)功能：负责下载指定url的html文本

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            print("url is None")
            return None
        response = urllib.request.urlopen(url)

        # 若正常，响应结果码是200
        if response.getcode() != 200:
            print('请求的url响应失败:' + url)
            return None
        return response.read()
