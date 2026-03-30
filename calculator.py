# Multiply function
def multiply_two_numbers(a, b):
    return a * b

# Subtract function
def subtract(a, b):
    return a - b

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call functions
multiplication_result = multiply_two_numbers(num1, num2)
subtraction_result = subtract(num1, num2)

# Print results
print("Multiplication =", multiplication_result)
print("Subtraction =", subtraction_result)