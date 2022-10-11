import random
from art import logo


def compare_numbers(estimated_number, hidden_number):
    if estimated_number == hidden_number:
        win = f"You got it! The answer was {hidden_number}."
        return win
    elif estimated_number < hidden_number:
        return f"Too low. Guess again."
    elif estimated_number > hidden_number:
        return f"Too high. Guess again."


def level_difficulty(x):
    if x == "easy":
        attempts = 10
    elif x == "hard":
        attempts = 5
    else:
        print("Invalid input. Type 'hard' or 'easy'")

    return attempts


new_number = random.randint(1, 100)
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = level_difficulty(difficulty)

for i in range(0, n):
    print(f"You have {n - i} attempts remaining to guess the number.")
    current_estimated_number = int(input("Make a guess: "))
    print(compare_numbers(current_estimated_number, new_number))
    if n - i == 1 and current_estimated_number != new_number:
        print("You've run out of guesses, you lose.")
    if current_estimated_number == new_number:
        break
