#Calculator
def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print("Result:", num1 + num2)
        elif operator == '-':
            print("Result:", num1 - num2)
        elif operator == '*':
            print("Result:", num1 * num2)
        elif operator == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
