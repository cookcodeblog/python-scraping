import csv

csv_file = open("./test.csv", "w+")
try:
    writer = csv.writer(csv_file)
    writer.writerow(("Number", "Number + 2", "Number * 2"))  # First row is header
    for i in range(10):
        writer.writerow((i, i + 2, i * 2))
finally:
    csv_file.close()  # Don't forget to close file

