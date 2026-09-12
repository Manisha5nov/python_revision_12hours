# Write a function to check whether a number is even or odd.
def check_even_odd(num):
    if num%2==0:
        return "Even"
    return "Odd"
n=int(input("Enter a number: "))
print(check_even_odd(n))