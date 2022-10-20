from data import MENU, resources

list_coins = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}


def check_request(current_answer):
    coins = []
    if current_answer in MENU:
        is_used_ingredients(current_answer)
        cost_of_drink = MENU[current_answer]["cost"]
        print("Please insert coins.")
        for coin in list_coins:
            coins.append(list_coins[coin] * int(input(f"How many {coin}? ")))

        sum_coins = sum(coins) / 100
        print(sum_coins)
        coins_check(sum_coins, cost_of_drink, current_answer)

    elif current_answer == "report":
        for item in resources:
            if item == "water" or item == "milk":
                print(f"{item}: {resources[item]}ml")
            elif item == "coffee":
                print(f"{item}: {resources[item]}g")
            else:
                print(f"{item}: ${resources[item]}")

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
    for ingredient in MENU[drink]["ingredients"]:
        required_volume = MENU[drink]["ingredients"][ingredient]
        left_volume = resources[ingredient]
        if required_volume <= left_volume:
            left_volume -= required_volume
        else:
            print(f"Sorry, there's not enough {ingredient}")

    # resources["water"] -= MENU[drink]["ingredients"]["water"]
    # resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    # resources["milk"] -= MENU[drink]["ingredients"]["milk"]


continue_flag = True

while continue_flag == True:
    answer_to_question = input("What whould you like? (espresso/latte/cappuccino)\n")
    check_request(answer_to_question)
