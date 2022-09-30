import random
import string

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)


number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like in your password? "))
number_of_digits = int(input("How many numbers would you like in your password? "))

password = ""

total_list = [letters, symbols, numbers]


for i in range(0, number_of_letters + 1):
    random_letters = random.choice(total_list[0])
    password += random_letters

for i in range(0, number_of_symbols + 1):
    random_symbols = random.choice(total_list[1])
    password += random_symbols

for i in range(0, number_of_digits + 1):
    random_digits = random.choice(total_list[2])
    password += random_digits

password = random.sample(password, len(password))

print("".join(password))
