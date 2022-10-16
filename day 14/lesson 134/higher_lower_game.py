from art import logo, vs
from data import data
import random

a = random.choice(data)
b = random.choice(data)

print(
    f'{logo}\nCompare A: {a["name"]}, a {a["description"]}, from {a["country"]}\n{vs}\nAgainst B: {b["name"]}, a {b["description"]}, from {b["country"]}'
)
