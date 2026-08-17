# sum of all the number from start to end by user divisible by 3 and 5
n= int (input("Enter the start number: "))
m= int (input("Enter the end number: "))
sum=0
i=n
while i <= m: 
    if i % 3 == 0 and i % 5 == 0:
        sum += i
    i += 1
print("Sum of numbers from", n, "to", m, "which is divisible by 3 and 5 is:", sum)