import random
from unicodedata import ucd_3_2_0


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
is_game_over = 0

if user_score > 21 or user_score == 0 or computer_score == 0:
    is_game_over = 1


while is_game_over == 1:

    answer_to_question = input("do you want to draw another card? y/n ")

    if answer_to_question == "y":
        is_game_over = 1
    else:
        is_game_over = 0
