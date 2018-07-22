from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

# lambda, function is an arg of another function
# tag is an input arg, and the return result is a boolean value
two_elements = bs_obj.findAll(lambda tag: len(tag.attrs) == 2)
for element in two_elements:
    print(element)
