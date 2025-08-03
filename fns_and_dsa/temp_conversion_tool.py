# Objective: Illustrate the concept of variable scope by creating a script that converts 
# temperatures between Celsius and Fahrenheit, using global variables to store conversion factors. 

# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main logic
def main():
    print("=== Temperature Conversion Tool ===")

    # Prompt for temperature input
    temp_input = input("Enter the temperature value: ").strip()

    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Prompt for temperature unit
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()

    # Process input and perform conversion
    if unit == 'c':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == 'f':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the program
if __name__ == "__main__":
    main() 

