# Function to get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function of the program
def basic_operations():
    print("Basic Operations Calculator")
    
    # Get the two numbers from the user
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Perform the operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Validate division to avoid division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error: Cannot divide by zero"

    # Print the results
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

# Execute the main function
basic_operations()
