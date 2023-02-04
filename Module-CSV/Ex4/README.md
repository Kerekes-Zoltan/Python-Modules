Write a Python program to read the current line from a given CSV file. Use csv.reader

open(file) function open the "employees.csv" with file as the "f". Call csv.reader(f) to generate an object which will iterate over each line in the given "employees.csv" file. Pass in the reader object to next(csv_reader) to get a single line from the .csv file.