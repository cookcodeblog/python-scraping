import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


pages = set()


def get_links(page_url):
    global pages
    url = "https://en.wikipedia.org" + page_url
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id="mw-content-text").findAll("p")[0])
        print(bs_obj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("Missed some attributes in page, but don't worry!")
    for link in bs_obj.findAll("a", {"href": re.compile("^(/wiki/)")}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # Only handle not duplicated links
                new_page = link.attrs['href']
                print("------------\n" + new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")
