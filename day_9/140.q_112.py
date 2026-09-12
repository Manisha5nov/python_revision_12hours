# Write a function to calculate the sum of digits.
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total
n=int(input("Enter a number: "))
print(sum_of_digits(n))