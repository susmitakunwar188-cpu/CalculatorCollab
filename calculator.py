# Multiply function
def multiply_two_numbers(a, b):
    return a * b

# Subtract function
def subtract(a, b):
    return a - b

# Division function
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call functions
multiplication_result = multiply_two_numbers(num1, num2)
subtraction_result = subtract(num1, num2)

# Print results
print("Subtraction =", subtraction_result)
print("Multiplication =", multiplication_result)
print("Division Result:", divide(num1, num2))