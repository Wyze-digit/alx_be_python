# Familiarize yourself with Python’s datetime module by writing a 
# script that performs specified operations with dates and times.

# import the date-time library from python standard library functions
import datetime
from datetime import datetime

# Function to display the current date and time 
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_current = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_current)
    return current_date  # Return the datetime object for further use

# Function to calculate and display the future date
def calculate_future_date(current_date, number_of_days):
    # Create a timedelta object using the number of days
    future_date = current_date + datetime.timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"The date after {number_of_days} days will be:", formatted_future)

# Main script execution
def main():
    # Step 1: Show current date/time
    current_date = display_current_datetime()

    # Step 2: Get number of days from user input
    try:
        number_of_days = int(input("Enter number of days to add: "))
        # Step 3: Calculate and display the future date
        calculate_future_date(current_date, number_of_days)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

if __name__ == "__main__":
    main() 

