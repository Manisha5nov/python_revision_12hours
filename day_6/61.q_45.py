# armstrong number is a number that is equal to the sum of its own digits 
# raised to the power of the numberof digits. 
# For example, 153 is an Armstrong number because it has 3 digits and 1^3 + 5^3 + 3^3 = 153. 

num = int(input("Enter a number: "))
temp = num
count = 0
armstrong_sum = 0
while temp > 0:
    temp //=10
    count +=1
print(f"The number of digits in {num} is: {count}")
temp=num
print(temp)
while temp >0:
    digit = temp % 10
    armstrong_sum += digit ** count
    temp //=10
if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")