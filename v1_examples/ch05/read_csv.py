import csv

csv_file = open("./test.csv", "rt")
csv_reader = csv.reader(csv_file, delimiter=',')
for row in csv_reader:
    print("|".join(row))



