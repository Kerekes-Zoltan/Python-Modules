import random

random.seed(0)
new_random_value = random.random()
print("Set a random seed and get a random number between 0 and 1: ", new_random_value)

random.seed(1)
new_random_value = random.random()
print("\nSet a random seed and get a random number between 0 and 1: ", new_random_value)

random.seed(2)
new_random_value = random.random()
print("\nSet a random seed and get a random number between 0 and 1: ", new_random_value)