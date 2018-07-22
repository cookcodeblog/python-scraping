from urllib.request import urlopen
from io import StringIO
import csv


url = "http://pythonscraping.com/files/MontyPythonAlbums.csv"
data = urlopen(url).read().decode('utf-8')
data_file = StringIO(data)  # CSV file in memory
csv_reader = csv.DictReader(data_file)


# print(csv_reader.fieldnames)
for row in csv_reader:
    print("The album {0} was released in {1}.".format(row['Name'], row['Year']))
