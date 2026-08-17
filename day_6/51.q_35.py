# print all the number which is divisible by 3 and 5 from start to end by user from 1 to 100

n= int (input("Enter the start number: "))
m= int (input("Enter the end number: "))
i=n
while i <= m:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1