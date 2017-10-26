import urllib.request

req = urllib.request.Request('http://news.baidu.com/')
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page)
