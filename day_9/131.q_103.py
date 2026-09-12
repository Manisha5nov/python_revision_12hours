# Write a function to find the largest of two numbers.

def largest(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal."
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))   
print(largest(f"largest number = {n} and {m}"))