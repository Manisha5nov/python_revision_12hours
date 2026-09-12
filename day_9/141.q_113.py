# Write a function to count digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
n=int(input("Enter a number: "))
print(count_digits(n))