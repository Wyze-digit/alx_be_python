#Objective: Implement a division calculator that robustly handles errors like division 
# by zero and non-numeric inputs using command line arguments.
#
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        if num < 0 or den < 0:
            return "Error: Only positive numbers are allowed."

        result = num / den
        return f"The result of the division is {result:.1f}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


