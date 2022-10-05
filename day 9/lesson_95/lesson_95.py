from art import logo

print(logo)
print("Welcome to the secret auction programm.")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_flag = True
bids = {}

while continue_flag == True:

    name = input("What is your name? ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    answer_to_question = input("Are there any other bidders? y/n ")

    if answer_to_question == "y":
        continue_flag = True
    else:
        continue_flag = False
        find_highest_bidder(bids)
