def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
num_1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

num_2 = int(input("What's the second number? "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num_1, num_2)

print(f"{num_1} {operation_symbol} {num_2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num_3 = int(input("What's the next number? "))

calculation_function = operations[operation_symbol]

second_answer = calculation_function(first_answer, num_3)

print(f"{first_answer} {operation_symbol} {num_3} = {second_answer}")
