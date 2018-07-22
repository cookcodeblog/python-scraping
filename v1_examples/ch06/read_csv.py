from urllib.request import urlopen
from io import StringIO
import csv


url = "http://pythonscraping.com/files/MontyPythonAlbums.csv"
data = urlopen(url).read().decode('utf-8')
data_file = StringIO(data)  # CSV file in memory
csv_reader = csv.reader(data_file)


for row in csv_reader:
    print(row)
