from data import MENU, resources

list_coins = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}
coins = []


def check_request(current_answer):
    if current_answer in MENU:
        cost_of_drink = MENU[current_answer]["cost"]
        print("Please insert coins.")
        for coin in list_coins:
            coins.append(list_coins[coin] * int(input(f"How many {coin}? ")))

        sum_coins = sum(coins) / 100
        coins_check(sum_coins, cost_of_drink, current_answer)

        is_used_ingredients(current_answer)
    elif current_answer == "report":
        print(resources)
    else:
        print("error")


def coins_check(current_sum, sum_of_drink, current_drink):
    if current_sum == sum_of_drink:
        print(f"Here's your {current_drink}. Enjoy!")
    elif current_sum > sum_of_drink:
        print(f"Your charge is {current_sum - sum_of_drink}")
        print(f"Here's your {current_drink}. Enjoy!")
    else:
        print("Sorry there is not enough money")
        print(f"{current_drink} costs {sum_of_drink}$. You inserted {current_sum}$")


def is_used_ingredients(drink):
    if drink == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif drink == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    elif drink == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    else:
        print("error")


answer_to_question = input("What whould you like? (espresso/latte/cappuccino)\n")
check_request(answer_to_question)
print(coins)
