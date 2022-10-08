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

continue_flag = 1

while continue_flag == 1:

    operation_symbol = input("Pick an operation: ")
    num_2 = int(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num_1, num_2)
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")

    if (
        input(f"type 'y' to continue calculation with {answer} or type 'n' to exit ")
        == "y"
    ):
        num_1 = answer
    else:
        continue_flag == 0
