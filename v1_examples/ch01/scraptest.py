from urllib.request import urlopen
url = "http://www.baidu.com"
html = urlopen(url)
print(html.read())
