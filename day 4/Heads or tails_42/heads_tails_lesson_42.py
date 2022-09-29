import random

test_seed = int(input("Create a seed number: "))
number = random.randint(0, 1)

if number == 1:
    print("Heads")
else:
    print("Tails")
