from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

images = bs_obj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image.attrs['src'])
