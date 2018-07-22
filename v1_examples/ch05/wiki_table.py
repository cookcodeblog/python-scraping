import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Comparison_of_text_editors"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")


table = bs_obj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")


csv_file = open("./wiki_table.csv", "wt", newline='', encoding='utf-8')
writer = csv.writer(csv_file)
try:
    for row in rows:
        csv_row = []
        for cell in row.findAll(['td', 'th']):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)
finally:
    csv_file.close()
