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
    if bigger_country == current_pair[0]:
        wrong_answer = current_pair[1]
    else:
        wrong_answer = current_pair[0]

    return wrong_answer


def find_smaller_area(y, first, second):
    if y == first:
        y = first
    else:
        y = second

    return y


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
first = countries_land_size[current_pair[0]]
second_country_area = countries_land_size[current_pair[1]]

my_answer = input(
    f"Чья площадь больше? {first_country} или {second_country}?\n\n{first_country} {vs} \n{second_country}\n\n"
)

bigger_area = compare_countries(first, second_country_area)
bigger_country = get_key(countries_land_size, bigger_area)
first = find_smaller_country(bigger_country, current_pair)
smaller_area = find_smaller_area(first, first, second_country_area)


print(
    f"{bigger_country} > {first}. {bigger_country} имеет площадь {bigger_area} км. Площадь {first} = {smaller_area} км. "
)


# if my_answer == countries_land_size[bigger_country]:
#     print(f"Да, правда, {bigger_country} с площадью {bigger_result} больше")
# else:
#     print(f"Нет, наоборот, {bigger_country} с площадью {bigger_result} больше")
