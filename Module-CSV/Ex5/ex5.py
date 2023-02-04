import csv

f = open("csv-file.csv", "r")
reader = csv.reader(f)
next(reader)

for row in reader:
    print(row)