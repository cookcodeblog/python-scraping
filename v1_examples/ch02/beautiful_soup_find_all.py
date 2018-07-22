from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")


# Print all green words
# 1st arg is tage, 2nd arg is a dictionary {key:value}
name_list = bs_obj.findAll("span", {"class": "green"})
for name in name_list:
    print(name.get_text())


# 4 objects in BeautifulSoup
#
# 1. BeautifulSoup object
# 2. Tag object
# 3. NavigableString object
# 4. Comment object
