import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)
lose = stages
word_dict = word_list

count_lose = 6
count_enter = 0

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
        count_lose -= 1
        if count_lose == -1:
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
