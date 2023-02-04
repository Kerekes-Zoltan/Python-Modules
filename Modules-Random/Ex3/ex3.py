import random
import string

print("Generate a random alphabetical character: ", random.choice(string.ascii_letters))

max_lenght = 100
str = ""
for i in range(random.randint(1, max_lenght)):
    str += random.choice(string.ascii_letters)
print("\nGenerate a random alphabetical string: ", str)

str = ""
for i in range(10):
    str += random.choice(string.ascii_letters)
print("\nGenerate a random alphabetical string of a fixed lenght: ", str)