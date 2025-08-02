# Multiplication operation. get user's input and perform mulplication of that input number from 1 to 10

# Ask the user to input a number
number = int(input("Enter a number to generate its multiplication table: "))

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

