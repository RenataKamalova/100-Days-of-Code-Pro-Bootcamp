import random
from art import logo
from art import vs


def compare_countries(first_country, second_country):
    if first_country > second_country:
        return "{first_country} больше {second_country} "
    else:
        return "{second_country} больше {first_country} "


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

print(current_pair)
my_answer = input(f"Чья площадь больше? {current_pair[0]} или {current_pair[1]}? ")

result = compare_countries(current_pair[0], current_pair[1])
print(result)
