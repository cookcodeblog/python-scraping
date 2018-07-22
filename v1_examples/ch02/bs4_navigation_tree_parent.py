from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

price = bs_obj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print(price)
