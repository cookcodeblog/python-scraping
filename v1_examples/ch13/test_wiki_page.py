from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TestWikipedia(unittest.TestCase):
    bs_obj = None

    def setUpClass():
        global bs_obj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bs_obj = BeautifulSoup(urlopen(url), "html.parser")

    def test_title(self):
        global bs_obj
        page_title = bs_obj.find("h1").get_text()
        self.assertEqual("Monty Python", page_title)

    def test_content_exists(self):
        global bs_obj
        content = bs_obj.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()