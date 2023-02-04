import csv

f = open("csv-file.csv", newline='')
reader = csv.reader(f)

print(next(reader))
print(next(reader))
print(next(reader))