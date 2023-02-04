import random

elements = range(0, 100)
num_list = random.sample(elements, 10)
print("Generate a list of random integers: ", num_list)

numb_elements = 4
rez = random.sample(num_list, numb_elements)
print("\nRandomly select", numb_elements, "multiple imtes from a list: ", rez)

numb_elements = 6
rez = random.sample(num_list, numb_elements)
print("\nRandomly select", numb_elements, "multiple imtes from a list: ", rez)