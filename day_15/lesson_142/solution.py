from data import MENU, resources


def check_request(current_answer):
    if current_answer in MENU:
        print("Please insert coins.")
        input("How many quarters?: \nHow many dimes?: \nHow many nickles?: \nHow many pennies?: ")
        if current_answer == "espresso":

    # elif current_answer == "latte":
    #     print("Please insert coins.")
    # elif current_answer == "cappuccino":
    #     print("Please insert coins.")
    elif current_answer == "report":
        check_resources(resources)
    else:
        print("error")


def check_resources(current_condition):
    return current_condition


answer_to_question = input("What whould you like? ")
check_request(answer_to_question)
