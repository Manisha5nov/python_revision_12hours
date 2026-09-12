# Write a function to divide two numbers.
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(divide(a, b))