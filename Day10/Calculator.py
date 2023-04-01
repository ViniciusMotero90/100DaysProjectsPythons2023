def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

function = operations["*"]
def calculator():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exist.: ") == 'y':
            num1 = answer
        else:
            should_continue = False

calculator()
