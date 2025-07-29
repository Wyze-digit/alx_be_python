# A Program for Simple Calculator using Match Case

# Call to get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask user for desired operation
operation = input("Choose the operation (+ , - , * , /): ")

# Perform calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
    case _:
        print("Invalid operation selected.")
