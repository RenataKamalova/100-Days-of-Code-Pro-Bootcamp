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
        result = "c"

    return result


def check(hypothesis, exact_answer):
    valid_answers = ["A", "a", "B", "b", "C", "c"]
    while hypothesis in valid_answers:
        if hypothesis == exact_answer:
            return True
        elif hypothesis != exact_answer:
            return False

    error = "incorrect input"
    return error


def game():
    continue_flag = True
    score = 0
    a = random.choice(data)

    while continue_flag == True and len(data) >= 1:
        b = random.choice(data)

        while a == b:
            b = random.choice(data)
        right_answer = compare(a, b)

        print(
            f'подсказка!\nчисло подписчиков у A) {a["name"]} = {a["follower_count"]},\nчисло подписчиков у B) {b["name"]} {b["follower_count"]}'
        )
        print(right_answer)

        print(
            f'{logo}\nCompare A: {a["name"]}, a {a["description"]}, from {a["country"]}\n{vs}\nAgainst B: {b["name"]}, a {b["description"]}, from {b["country"]}'
        )
        my_answer = input(
            "Who has more followers? Type 'A' or 'B' or 'C' (if they have equal number of followers)'\n"
        ).lower()

        if check(my_answer, right_answer) == True:
            score += 1
            print(f"You're right! Current score: {score}")
            a = b

        elif check(my_answer, right_answer) == False:
            score = 0
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_flag = False
        else:
            print(check(my_answer, right_answer))
            data.append(b)


game()
"""
придумать функцию для проверки. соединить в одно

сделать функциональность такую чтобы повторялся один и тот же аккаунт сравнивался с другими

сделать функцию format_data, которая будет отдельно рассматривать name descriptiom country and count_followers
"""
