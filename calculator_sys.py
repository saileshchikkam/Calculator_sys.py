import os
import calc_ASCII
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calc_ASCII.logo)
    first_number = float(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        operation = input("Pick an operation from the above once: ")
        next_number = float(input("Enter the next number: "))
        calculator_function = operations_dict[operation]
        output = calculator_function(first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {output}")

        should_continue = input(
            f"Enter 'y' to continue calculations with {output} "
            f"or 'n' to start a new calculation,"
            f"or 'x' to out from calculator: \n").lower()
        if should_continue == 'y':
            first_number = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("Exit")

calculator()
