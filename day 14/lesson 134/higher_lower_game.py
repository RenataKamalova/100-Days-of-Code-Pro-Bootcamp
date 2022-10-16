from turtle import right
from art import logo, vs
from data import data
import random


def compare(first_person, second_person):
    if first_person["follower_count"] > second_person["follower_count"]:
        result = first_person["name"]
    elif second_person["follower_count"] > first_person["follower_count"]:
        result = second_person["name"]
    else:
        result = "equal number"

    return result


a = random.choice(data)
b = random.choice(data)

right_answer = compare(a, b)

print(
    f'{logo}\nCompare A: {a["name"]}, a {a["description"]}, from {a["country"]}\n{vs}\nAgainst B: {b["name"]}, a {b["description"]}, from {b["country"]}'
)
my_answer = input("Who has more followers? Type 'A' or 'B' ")

print(right_answer)
