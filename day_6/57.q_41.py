# ask a number from the user and count factors of that number using while loop

num = int(input("Enter a number: "))
count = 0
i=1
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
print(f"The number of factors of {num} is: {count}")