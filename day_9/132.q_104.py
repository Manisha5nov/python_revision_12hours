# Write a function to find the largest of three numbers.
def largest_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
p=int(input("Enter third number: "))
print(largest_of_three(n,m,p))