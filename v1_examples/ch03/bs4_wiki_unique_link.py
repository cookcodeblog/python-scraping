import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


pages = set()


def get_links(page_url):
    global pages
    url = "https://en.wikipedia.org" + page_url
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")
    for link in bs_obj.findAll("a", {"href": re.compile("^(/wiki/)")}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # Only handle not duplicated links
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")
