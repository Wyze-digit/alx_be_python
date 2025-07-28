# Objective: Use user input, variables, and arithmetic operations to calculate and provide
# feedback on a user’s monthly savings and potential future savings without applying conditional statements.

# Ask the user for their current monthly income
monthly_income = int(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expense = int(input("Enter your monthly Expenses: "))

# calculate monthly savings for user
monthly_savings = monthly_income - monthly_expense

# declare annual interest rate
annual_interest = 0.05

# calculate the projected savings for the year
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Display the monthly savings and annual savings
print(f"Your Monthly Savings are {monthly_savings}")

print(f"Projected Savings after one year, with interest, is: {projected_savings}")

