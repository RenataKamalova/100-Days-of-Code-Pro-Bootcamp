from operator import le
import random

lose = [
    """
   _____
  +     +
        |
        |
        |
        |
        |
""",
    """
   _____
  +     +
  O     |
        |
        |
        |
        |
""",
    """
   _____
  +     +
  O     |
  |     |
        |
        |
        |
""",
    """
   _____
  +     +
  O     |
 /|     |
        |
        |
        |
""",
    """
   _____
  +     +
  O     |
 /|\    |
        |
        |
        |
""",
    """
   _____
  +     +
  O     |
 /|\    |
   \    |
        |
        |
""",
    """
   _____
  +     +
  O     |
 /|\    |
 / \    |
        |
        |
""",
]

count_lose = 0

word_dict = ["programmer", "table", "computer"]

word = random.choice(word_dict)

empty_word = []

for i in range(0, len(word)):
    empty_word.append("_")

print(" ".join(empty_word))
print()

while "_" in empty_word:
    letter = input("Угадайте букву:\n").lower()
    print()
    if letter not in word:
        print("\nНеверно", lose[count_lose])
        count_lose += 1
        if count_lose == 6:
            print("Ты проиграл")
            break
    else:
        print("Есть такая буква\n")

    for i in range(0, len(word)):
        if letter == word[i]:
            empty_word[i] = letter

    print(" ".join(empty_word))
    print()

if "_" not in empty_word:
    print("You are genius")
