import random

names_string = input("Введите имена через запятую ")
names = names_string.split(", ")

choice = random.randint(0, len(names) - 1)

print(f"Платить будет {names[choice]}")
