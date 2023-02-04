import random

print("Construct a seeded random number: ", random.Random().random(), " ", random.Random(0).random())
print("\nGenerate a float between 0 and 1: ", random.random())