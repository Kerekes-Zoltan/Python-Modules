import csv

file_w = open("csv-file.csv", "w", newline='')
writer = csv.DictWriter(file_w, fieldnames=["Name", "Age"])
writer.writeheader()
writer.writerows([{"Name": "Kerekes Zoltan", "Age": "23"},
                  {"Name": "Becsky Tamas", "Age": "22"},
                  {"Name": "Cornea Andra", "Age": "21"}])
file_w.close()

file_r = open("csv-file.csv", "r")
csv = csv.reader(file_r, delimiter=",")
for row in csv:
    print(row)
    
file_r.close()