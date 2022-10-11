import random
from art import logo


def compare_numbers(estimated_number, hidden_number):
    if estimated_number < hidden_number:
        return f"Too low. Guess again."
    elif estimated_number > hidden_number:
        return f"Too high. Guess again."
    else:
        return f"You got it! The answer was {hidden_number}."


def level_difficulty(x):
    if x == "easy":
        return 10
    elif x == "hard":
        return 5
    else:
        return 0


answer = random.randint(1, 100)
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = level_difficulty(difficulty)

if n == 0:
    print("Invalid input. Type 'hard' or 'easy'")

print(f"число = {answer}")

for i in range(0, n):
    print(f"You have {n - i} attempts remaining to guess the number.")
    current_estimated_number = int(input("Make a guess: "))
    print(compare_numbers(current_estimated_number, answer))
    if n - i == 1 and current_estimated_number != answer:
        print(f"You've run out of guesses, you lose. The answer was {answer}")
    if current_estimated_number == answer:
        break
