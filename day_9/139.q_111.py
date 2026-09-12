# Write a function to check palindrome number.
def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num

n = int(input("Enter a number: "))
print(is_palindrome(n))
