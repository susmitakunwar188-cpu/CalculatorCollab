# Multiplication function
def multiply_two_numbers(a, b):
    return a * b

# Division function
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call functions and display results
print("Multiplication Result:", multiply_two_numbers(num1, num2))
print("Division Result:", divide(num1, num2))