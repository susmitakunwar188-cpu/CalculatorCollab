# Division Calculator 

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Take input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call function and display result
print("Division Result:", divide(num1, num2))