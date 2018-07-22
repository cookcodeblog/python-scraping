from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

# children, not children()
# case sensitive, can't write "gitList" as 'gitlist"
for child in bs_obj.find("table", {"id": "giftList"}).children:
    print(child)
