# sum of all the numbers from start to end by user

n= int (input("Enter the start number: "))
m= int (input("Enter the end number: "))
sum=0
i=n
while i <= m:
    sum += i
    i += 1
print("Sum of numbers from", n, "to", m, "is:", sum)