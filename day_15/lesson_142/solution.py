from data import MENU, resources

list_coins = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}
resources["money"] = 0


def check_request(current_answer):
    coins = []
    if current_answer in MENU:
        if is_used_ingredients(current_answer) == True:
            cost_of_drink = MENU[current_answer]["cost"]
            print("Please insert coins.")
            for coin in list_coins:
                how_many_coins = int(input(f"How many {coin}? "))
                coins.append(list_coins[coin] * how_many_coins)
            print(f"You inserted ${sum(coins)}")
            coins_check(sum(coins), cost_of_drink, current_answer)
        else:
            insufficient_ingredient = is_used_ingredients(current_answer)
            print(f"Sorry, there's not enough {insufficient_ingredient}")

    elif current_answer == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${resources['money']}")

    elif current_answer == "off":
        return False
    else:
        print("error, check spelling please")


def coins_check(current_sum, sum_of_drink, current_drink):

    if current_sum == sum_of_drink:
        print(f"Here's your {current_drink}. Enjoy!")
        resources["money"] += current_sum
    elif current_sum > sum_of_drink:
        print(f"Here's ${round(current_sum - sum_of_drink,2)} in change")
        print(f"Here's your {current_drink}. Enjoy!")
        resources["money"] += sum_of_drink
    else:
        print("Sorry there is not enough money")
        print(f"{current_drink} costs {sum_of_drink}$. You inserted {current_sum}$")


def is_used_ingredients(drink):

    for ingredient in resources:
        if ingredient in MENU[drink]["ingredients"]:
            required_volume = MENU[drink]["ingredients"][ingredient]
            left_volume = resources[ingredient]
            if required_volume <= left_volume:
                left_volume -= required_volume
                resources[ingredient] = left_volume
            else:
                return ingredient

    return True


condition_is_on = True

while condition_is_on == True:
    answer_to_question = input("What whould you like? (espresso/latte/cappuccino)\n")
    result = check_request(answer_to_question)
    if result == False:
        condition_is_on = False
