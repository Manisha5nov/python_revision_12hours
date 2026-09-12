# Write a function to reverse a number.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
n=int(input("Enter a number: "))
print(reverse_number(n))