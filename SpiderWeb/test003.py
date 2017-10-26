#**********  coding: UTF-8  ***********
# 主要功能是将抓取到的百度翻译的界面解码成主要可观的语句
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    html = html.decode("utf-8")
    print(html)
