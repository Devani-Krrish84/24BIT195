def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero is not allowed"

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("The sum is:", add(num1, num2))
print("The difference is:", subtract(num1, num2))
print("The product is:", multiply(num1, num2))
print("The quotient is:", divide(num1, num2))