from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://pythonscraping.com/"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")
image_location = bs_obj.find("a", {"id": "logo"}).find("img").attrs['src']

# urlretieve method doesn't know to create a new directory
urlretrieve(image_location, "logo.jpg")
