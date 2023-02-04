import copy

original_dictionary = {"a":1, "b":2, 'cc':{"c":3}}
copy_dictionary = copy.deepcopy(original_dictionary)

print("Original directory: ", original_dictionary)
print("Deep copy of the original directory: ", copy_dictionary)

original_dictionary["cc"]["c"] = 24
print("\nChange value of an element of the original directory: ", original_dictionary)
print("Second directory (Deep Copy): ", copy_dictionary)

dictionary = {"x":1, "y":2, 'zz':{"z":3}}
copy_dic = copy.deepcopy(dictionary)
print("\nOriginal Directory: ", dictionary)
print("Deep copy of the Directory: ", copy_dic)

dictionary["zz"]["z"] = 240
print("\nChange value of an element of the original Directory: ", dictionary)
print("First dictionary: ", dictionary)
print("Second dictionary (Deep Copy): ", copy_dic)