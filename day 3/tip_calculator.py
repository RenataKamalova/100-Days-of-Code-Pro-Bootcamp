input('Welcome to the tip calculator!')
totall_bill = float(input("What was the total bill?"))
percent_tip = int(input("How much tip would you like to give?"))
number_of_people = int(input("How many people to split the bill?"))

sum_number = totall_bill / number_of_people
result = round(
    ((totall_bill * (percent_tip / 100)) / number_of_people) + sum_number, 2)

print(f'Each person should pay: {result}')
