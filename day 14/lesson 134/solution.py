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
    if x == pair[0]:
        x = pair[1]
    else:
        x = pair[0]

    return x


def find_smaller_area(y, first, second):
    if y == first:
        y = first
    else:
        y = second

    return y


print(logo)
countries_land_size = {}
pair = []


with open("countries.txt") as file:
    for line in file:
        [country, land_size] = line.split(",")
        countries_land_size[country] = int(land_size)

all_countries = list(countries_land_size.keys())


for i in range(2):
    country = random.choice(all_countries)
    pair.append(country)

first_country = pair[0]
second_country = pair[1]
first_country_area = countries_land_size[pair[0]]
second_country_area = countries_land_size[pair[1]]

my_answer = input(
    f"Чья площадь больше? {first_country} или {second_country}?\n\n{first_country} {vs} \n{second_country}\n\n"
)

bigger_area = compare_countries(first_country_area, second_country_area)
bigger_country = get_key(countries_land_size, bigger_area)
smaller_country = find_smaller_country(bigger_country, pair)
smaller_area = find_smaller_area(
    smaller_country, first_country_area, second_country_area
)


print(
    f"{bigger_country} > {smaller_country}. {bigger_country} имеет площадь {bigger_area} км. Площадь {smaller_country} = {smaller_area} км. "
)


if my_answer == countries_land_size[bigger_country]:
    print(f"Да, правда, {bigger_country} с площадью {bigger_result} больше")
else:
    print(f"Нет, наоборот, {bigger_country} с площадью {bigger_result} больше")
