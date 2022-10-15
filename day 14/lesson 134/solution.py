from multiprocessing.sharedctypes import Value
import random
from telnetlib import PRAGMA_HEARTBEAT
from art import logo
from art import vs


def compare_countries(first, second):
    if first > second:
        result = first
    else:
        result = second

    return result


print(logo)
countries_land_size = {}
current_pair = []


with open("countries.txt") as topo_file:
    for line in topo_file:
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

for key in countries_land_size:
    if countries_land_size[key] == right_answer:
        print(key)


# if my_answer == countries_land_size[right_answer]:
#     print(f"Да, правда, {right_answer} с площадью больше")
# else:
#     print(f"Нет, наоборот, {right_answer} больше")
