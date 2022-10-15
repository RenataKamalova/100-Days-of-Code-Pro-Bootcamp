import random
from art import logo
from art import vs


def compare_countries(first, second):
    if first > second:
        result = first
    else:
        result = second

    return result


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(logo)
countries_land_size = {}
current_pair = []


with open("countries.txt") as file:
    for line in file:
        [country, land_size] = line.split(",")
        countries_land_size[country] = int(land_size)

all_countries = list(countries_land_size.keys())


for i in range(2):
    country = random.choice(all_countries)
    current_pair.append(country)

first_country = current_pair[0]
second_country = current_pair[1]
first_country_area = countries_land_size[current_pair[0]]
second_country_area = countries_land_size[current_pair[1]]

# my_answer = input(
#     f"Чья площадь больше? {first_country} или {second_country}?\n\n{first_country} {vs} \n{second_country}\n\n"
# )

right_answer = compare_countries(first_country_area, second_country_area)
x = get_key(countries_land_size, right_answer)
print(x)


# if my_answer == countries_land_size[right_answer]:
#     print(f"Да, правда, {right_answer} с площадью больше")
# else:
#     print(f"Нет, наоборот, {right_answer} больше")
