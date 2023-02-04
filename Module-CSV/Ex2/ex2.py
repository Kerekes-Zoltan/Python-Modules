import csv

reader = csv.reader(open("csv-file.csv"))

cnt_lines = len(list(reader))
print("Number of lines in a given CSV file: ", cnt_lines)