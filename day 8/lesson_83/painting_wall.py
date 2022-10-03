from math import ceil
from turtle import width


def counting_cans(height, width, coverage):
    print(ceil((height * width) / coverage))


counting_cans(height=int(input("Height = ")), width=int(input("Width = ")), coverage=5)
