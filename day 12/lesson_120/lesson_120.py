import random
from art import logo


def compare_numbers(estimated_number, hidden_number):
    if estimated_number < hidden_number:
        return f"Too low. Guess again."
    elif estimated_number > hidden_number:
        return f"Too high. Guess again."
    else:
        return f"You got it! The answer was {hidden_number}."


def set_difficulty(lvl):
    if lvl == "easy":
        return 10
    elif lvl == "hard":
        return 5
    else:
        return 0


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")

answer = random.randint(1, 100)
hard_easy_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = set_difficulty(hard_easy_level)

if n == 0:
    print("Invalid input. Type 'hard' or 'easy'")


for i in range(0, n):
    print(f"You have {n - i} attempts remaining to guess the number.")
    current_estimated_number = int(input("Make a guess: "))
    print(compare_numbers(current_estimated_number, answer))
    if n - i == 1 and current_estimated_number != answer:
        print(f"You've run out of guesses, you lose. The answer was {answer}")
    if current_estimated_number == answer:
        break
