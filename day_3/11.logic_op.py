'''what is logic operators in python?
Logic operators in Python are used to combine multiple boolean expressions and return a boolean result (True or False). 
They are commonly used in conditional statements and loops to control the flow of a program based on multiple conditions. 
The logical operators in Python include:
1. and: Returns True if both expressions are True.
2. or: Returns True if at least one of the expressions is True.
3. not: Returns True if the expression is False, and returns False if the expression is True.
'''

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Logical AND:", num1 > 0 and num2 > 0)
print("Logical OR:", num1 > 0 or num2 > 0)
print("Logical NOT:", not(num1 > 0))
