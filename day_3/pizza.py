print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    total_sum = 15
    if add_pepperoni == "Y":
        total_sum += 2         
    if extra_cheese == "Y":
        total_sum += 1
elif size == "M":
    total_sum = 20
    if add_pepperoni == "Y":
        total_sum += 3    
    if extra_cheese == "Y":
        total_sum += 1
else:
    total_sum = 25
    if add_pepperoni == "Y":
        total_sum += 3
    if extra_cheese == "Y":
        total_sum += 1

print(f"Your final bill is: ${total_sum}.")