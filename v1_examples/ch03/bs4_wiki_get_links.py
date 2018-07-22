import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


random.seed(datetime.datetime.now())


def get_links(article_url):
    url = "https://en.wikipedia.org" + article_url
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")
    return bs_obj.find("div", {"id": "bodyContent"})\
        .findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")})


links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
