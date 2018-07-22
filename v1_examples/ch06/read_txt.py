from urllib.request import urlopen


text_page = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# The response is text format instead of html format, so don't need BeautifulSoup object
print(text_page.read())
