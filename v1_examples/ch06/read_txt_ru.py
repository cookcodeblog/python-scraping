from urllib.request import urlopen


# Russian text
text_page = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# The response is text format instead of html format, so don't need BeautifulSoup object
#print(text_page.read().decode("utf-8"))
print(str(text_page.read(), "utf-8"))
