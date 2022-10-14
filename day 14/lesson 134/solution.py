import random
from art import logo
from art import vs

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
