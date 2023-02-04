import csv

reader = csv.reader(open("csv-file.csv"))

for row in reader:
    print(row)