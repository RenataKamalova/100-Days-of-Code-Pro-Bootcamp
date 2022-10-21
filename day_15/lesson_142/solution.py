from data import MENU, resources

list_coins = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}


def check_request(current_answer):
    coins = []
    if current_answer in MENU:
        if is_used_ingredients(current_answer) == True:
            cost_of_drink = MENU[current_answer]["cost"]
            print("Please insert coins.")
            for coin in list_coins:
                how_many_coins = int(input(f"How many {coin}? "))
                coins.append(list_coins[coin] * how_many_coins)

            sum_coins = sum(coins) / 100
            print(f"You inserted ${sum_coins}")
            coins_check(sum_coins, cost_of_drink, current_answer)
        else:
            insufficient_ingredient = is_used_ingredients(current_answer)
            print(f"Sorry, there's not enough {insufficient_ingredient}")

    elif current_answer == "report":
        for item in resources:
            if item == "water" or item == "milk":
                print(f"{item}: {resources[item]}ml")
            elif item == "coffee":
                print(f"{item}: {resources[item]}g")
            else:
                print(f"{item}: ${resources[item]}")

    elif current_answer == "off":
        return False
    else:
        print("error, check spelling please")


def coins_check(current_sum, sum_of_drink, current_drink):
    resources["money"] = 0
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
    check_request(answer_to_question)
    if check_request(answer_to_question) == False:
        condition_is_on = False
