import random
from art import logo
from art import vs

countries_land_size = {}

with open("countries.txt") as topo_file:
    for line in topo_file:
        [country, land_size] = line.split(",")
        countries_land_size[country] = int(land_size)

all_countries = list(countries_land_size.keys())
country_1 = random.choice(all_countries)
country_2 = random.choice(all_countries)

print(f"{country_1} = {countries_land_size[country_1]}")
print(f"{country_2} = {countries_land_size[country_2]}")
