import csv


csv_text = """1, 2, 3,
4, 5, 6,
7, 8, 9
"""
            
print("Original text: ", csv_text)

lines = csv_text.splitlines()
print("List of CSV formatted texts: ", lines)

reader  = csv.reader(lines)
parsed_csv = list(reader)
print("\nList representation of the CSV file: ", parsed_csv)