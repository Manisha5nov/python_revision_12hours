# Write a function to remove spaces from a string.

def remove_spaces(s):
    return s.replace(" ", "")   

n = input("Enter a string: ")
print(remove_spaces(n))