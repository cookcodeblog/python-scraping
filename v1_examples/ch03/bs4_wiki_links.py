from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

links = bs_obj.find("div", {"id": "bodyContent"}).findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")})
# default is 671 links
print(len(links))
for link in links:
    if "href" in link.attrs:
        print(link.attrs['href'])

