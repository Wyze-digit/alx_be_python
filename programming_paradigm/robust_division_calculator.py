#Objective: Implement a division calculator that robustly handles errors like division 
# by zero and non-numeric inputs using command line arguments.
#
def safe_divide(numerator, denominator):
    try:
        # Attempt conversion to float
        num = float(numerator)
        den = float(denominator)

        # Check for positive values
        if num <= 0 or den <= 0:
            return "Error: Only positive numbers are allowed."

        # Perform division
        result = num / den
        return f"Result: {result:.2f}"

    except ValueError:
        return "Error: Both inputs must be numeric."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


