# create table of 1 to 10 using while loop

num = int(input("Enter the number for which you want to create a multiplication table: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1