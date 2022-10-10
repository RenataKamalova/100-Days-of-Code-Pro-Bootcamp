import random


def create_number():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    x = random.choice(numbers)
    return x


def compare_numbers(estimated_number, hidden_number):
    if estimated_number == hidden_number:
        win = f"You got it! The answer was {hidden_number}."
        return win
    elif estimated_number < hidden_number:
        return f"Too low. Guess again."
    elif estimated_number > hidden_number:
        return f"Too high. Guess again."


new_number = create_number()

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    for i in range(0, 10):
        print(f"You have {10 - i} attempts remaining to guess the number.")
        current_estimated_number = int(input("Make a guess: "))
        print(compare_numbers(current_estimated_number, new_number))
        if 10 - i == 1 and current_estimated_number != new_number:
            print("You've run out of guesses, you lose.")
        if current_estimated_number == new_number:
            break


elif difficulty == "hard":
    for i in range(0, 5):
        print(f"You have {5 - i} attempts remaining to guess the number.")
        current_estimated_number = int(input("Make a guess: "))
        print(compare_numbers(current_estimated_number, new_number))
        if 5 - i == 1 and current_estimated_number != new_number:
            print("You've run out of guesses, you lose.")
        if current_estimated_number == new_number:
            break

else:
    print("Invalid input. Type 'hard' or 'easy'")
