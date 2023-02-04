import csv

file_w = open("csv-file.csv", "w", newline='')
writer = csv.writer(file_w, delimiter = ",")
writer.writerow(["a", "b", "c"])
writer.writerow(["d", "e", "f"])
writer.writerow(["g", "h", "i"])
file_w.close()

file_r = open("csv-file.csv", "r")
csv = csv.reader(file_r, delimiter = ",")

for row in csv:
    print(row)
    
file_r.close()