def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2


print("Simple calculator")

n1 = float(input("Enter first number: "))
keep_going = True

while keep_going:
    operator = input("Enter an operator (+, -, *, /): ")
    n2 = float(input("Enter second number: "))

    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        try:
            result = divide(n1, n2)
        except ValueError as e:
            print(e)
            continue
    else:
        print("Invalid operator")
        continue

    print(f"{n1} {operator} {n2} = {result}")

    choice = input("Type 'y' to continue calculating with this result, or 'n' to stop: ")

    if choice.lower() == "y":
        n1 = result
    else:
        keep_going = False
