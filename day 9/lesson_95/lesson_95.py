from art import logo

print(logo)
print("Welcome to the secret auction programm.")


def auction_dict(participant, value):
    auction = {
        participant: value,
    }
    print(auction)


continue_flag = True

while continue_flag == True:

    name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    answer_to_question = input("Are there any other bidders? Y/N ")

    if answer_to_question == "Y":
        continue_flag = True
    else:
        continue_flag = False

auction_dict(name, bid)
