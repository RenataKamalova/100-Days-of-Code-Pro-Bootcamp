import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

items = ["rock", "paper", "scissors"]


sum_first = 0
sum_second = 0
move = 1

while sum_second < 3 and sum_first < 3:
    my_choice = input("Вы: ")
    second_player = random.choice(items)
    print(f"Компьютер: {second_player}")

    if my_choice != second_player:
        move += 1

        if (
            (my_choice == "scissors" and second_player == "paper")
            or (my_choice == "paper" and second_player == "rock")
            or (my_choice == "rock" and second_player == "scissors")
        ):
            sum_first += 1
            print(f"Ура! Счёт - {sum_first}:{sum_second}")
        else:
            sum_second += 1
            print(f"Ой:(. Счёт - {sum_first}:{sum_second}")
    else:
        print(f"Счёт - {sum_first}:{sum_second}")

if sum_second == 3 or sum_first == 3:
    if sum_first > sum_second:
        print(f"Вы победили!")
    elif sum_second > sum_first:
        print("Победил компьютер")
    else:
        print("Ничья")
