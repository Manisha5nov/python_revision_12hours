# armstrong number is a number that is equal to the sum of its own digits 
# raised to the power of the number of digits. For example, 
# 153 is an Armstrong number because it has 3 digits and 1^3 + 5^3 + 3^3 = 153.

from unicodedata import digit


num = int(input("Enter a number: "))
# Find the number of digits in the number
temp = num
count = 0
sum = 0
while temp>0:
    temp//=10
    count+=1
print(f"Number of digits in {num}: {count}")
    