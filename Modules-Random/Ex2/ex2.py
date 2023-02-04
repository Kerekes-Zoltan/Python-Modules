import random
import os

element = [1, 2, 3, 4, 5, 6]
print("Select random elements from a list: ", random.choice(element), " ", random.choice(element))

element = set([1, 2, 3, 4, 5, 6])
print("\nSelect a random elements from a set: ", random.choice(tuple(element)), " ", random.choice(tuple(element)))

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
key = random.choice(list(dictionary))

print("\nSelect a random element from a dictionary: ", dictionary[key], " ", dictionary[key], " ", dictionary[key])

print("\nSelect a random file from a directory: ", random.choice(os.listdir("/")))