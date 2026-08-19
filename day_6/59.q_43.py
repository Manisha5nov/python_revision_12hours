# count the number of digits in a number


num = int(input("Enter a number: "))
# Find the number of digits in the number
temp = num
count = 0
while temp>0:
    temp//=10
    count+=1
print(f"Number of digits in {num}: {count}")
    