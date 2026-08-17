# asl number  from the user and print  all the factors of that number using while loop

num = int(input("Enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
    