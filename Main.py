import urllib.request

getBaidu=urllib.request.urlopen("http://www.baidu.com")
pageGet=getBaidu.read()
print(pageGet)

print("怎么去爬一个网站的内容呢？")
