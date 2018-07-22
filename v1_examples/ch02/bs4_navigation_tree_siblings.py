from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

# next_siblings don't gave "title" row
for sibling in bs_obj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
