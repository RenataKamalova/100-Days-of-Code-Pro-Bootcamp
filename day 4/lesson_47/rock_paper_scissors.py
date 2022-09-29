import random

list_items = ["rock", "paper", "scissors"]

sum_first = 0
sum_second = 0
move = 1

while sum_second < 3 and sum_first < 3:

    first_player = random.choice(list_items)
    second_player = random.choice(list_items)

    if first_player != second_player:

        print(
            f"{move} ход: первый игрок - {first_player}, второй игрок - {second_player}"
        )
        move += 1

        if (
            (first_player == "scissors" and second_player == "paper")
            or (first_player == "paper" and second_player == "rock")
            or (first_player == "rock" and second_player == "scissors")
        ):
            sum_first += 1
        else:
            sum_second += 1

if sum_second == 3 or sum_first == 3:
    if sum_first > sum_second:
        print(
            f"победил первый игрок c суммой очков {sum_first} против второго игрока с суммой очков {sum_second}"
        )
    elif sum_second > sum_first:
        print("победил второй игрок")
    else:
        print("ничья")
