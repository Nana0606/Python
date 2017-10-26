from urllib import parse

url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B%22search%22%3A%22%E5%8D%A2%E5%8D%AB%20%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E5%A4%A7%E5%AD%A6%22%2C%22sType%22%3A%22writer%22%7D&"

urlTmp1 = url.replace("http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B%22search%22%3A%22", "")
urlTmp2 = urlTmp1.replace("%22%2C%22sType%22%3A%22writer%22%7D&", "")
print('new1: ', urlTmp1)
print('new2: ', urlTmp2)
