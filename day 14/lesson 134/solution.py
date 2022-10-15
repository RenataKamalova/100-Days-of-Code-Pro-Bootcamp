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


def find_smaller_country(x, pair):
    if right_answer == current_pair[0]:
        wrong_answer = current_pair[1]
    else:
        wrong_answer = current_pair[0]

    return wrong_answer


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

bigger_result = compare_countries(first_country_area, second_country_area)
right_answer = get_key(countries_land_size, bigger_result)
smaller_country = find_smaller_country(right_answer, current_pair)

print(smaller_country)
# print(f"{bigger_result} c площадью {bigger_result}> {smaller_country}")


if my_answer == countries_land_size[right_answer]:
    print(f"Да, правда, {right_answer} с площадью {bigger_result} больше")
else:
    print(f"Нет, наоборот, {right_answer} с площадью {bigger_result} больше")
