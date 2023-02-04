import copy

original_directory = {"a":1, "b":2, "cc":{"c":3}}
print("Original directory: ", original_directory)

copy_directory = copy.copy(original_directory)
print("Copy directory: ", copy_directory)

original_directory["cc"]["c"] = 10
print("\nChange the value of an element of the original directory: ", original_directory)
print("Copy directory: ", copy_directory)

directory = {"x":1, "y":2, "zz":{"z":3}}
copy_directory = copy.copy(directory)
print("\nOriginal directory: ", directory)
print("Copy directory: ", copy_directory)

directory ["zz"]["z"] = 24
print("\nChange the value of an element of the original directory: ",directory)
print("First directory: ", directory)
