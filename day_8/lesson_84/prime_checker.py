def prime_checker(number):
    if (
        number > 10
        and number % 2 != 0
        and number % 3 != 0
        and number % 5 != 0
        and number % 7 != 0
    ):
        print("It's a prime number.")
    elif number == 2 or number == 3 or number == 5 or number == 7:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
