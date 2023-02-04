import random
import string

print("Generate a random color in hex: ", "#{:06x}".format(random.randint(0, 0xFFFFFF)))

max_lenght = 255
s = ""
for i in range(random.randint(1, max_lenght)):
    s += random.choice(string.ascii_letters)
print("\nGenerate a random alphabetical string: ", s)

print("\nGenerate a random number between two integers: ", random.randint(0,24), " ", random.randint(-5, 5), " ", random.randint(-9, 0))

print("\nGenerate a random multiple of 7 between 0 and 70: ", random.randint(0, 10) * 7)