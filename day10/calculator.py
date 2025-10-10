# Calculator
# add
def add(n1, n2):
    return n1 + n2
# subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    continue_program = True
    while continue_program:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to exit: ") == "y":
            num1 = answer
        else:
            continue_program = False
            calculator()

calculator()
