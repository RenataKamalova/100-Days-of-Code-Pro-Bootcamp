from turtle import right
from art import logo, vs
from data import data
import random


def compare(first_person, second_person):
    if first_person["follower_count"] > second_person["follower_count"]:
        result = first_person["name"]
        result = "a"
    elif second_person["follower_count"] > first_person["follower_count"]:
        result = second_person["name"]
        result = "b"
    else:
        result = "equal number"

    return result


def game():
    continue_flag = True
    score = 0
    while continue_flag == True:

        a = random.choice(data)
        b = random.choice(data)
        # score = 0

        right_answer = compare(a, b)

        print(
            f'подсказка!\nчисло подписчиков у A) {a["name"]} = {a["follower_count"]},\nчисло подписчиков у B) {b["name"]} {b["follower_count"]}'
        )
        print(right_answer)

        print(
            f'{logo}\nCompare A: {a["name"]}, a {a["description"]}, from {a["country"]}\n{vs}\nAgainst B: {b["name"]}, a {b["description"]}, from {b["country"]}'
        )
        my_answer = input("Who has more followers? Type 'A' or 'B'\n").lower()

        if my_answer == right_answer:
            score += 1
            print(f"You're right! Current score: {score}")
        elif my_answer != right_answer:
            score = 0
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_flag = False
        else:
            print("Incorrect input")


game()
