from urllib import request
html = request.urlopen("http://www.baidu.com").read()
print(html)
