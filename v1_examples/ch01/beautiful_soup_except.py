from urllib.request import  urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(_url):
    try:
        html = urlopen(_url)
    except (HTTPError, URLError):
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), "html.parser")
        _title = bs_obj.body.h1
    except AttributeError:
        return None
    return _title


url = "http://www.pythonscraping.com/pages/page1.html"
# url = "http://www.pythonscraping.com/pages/page1-none.html"
title = get_title(url)
if title is None:
    print("Title could not be found")
else:
    print(title)
