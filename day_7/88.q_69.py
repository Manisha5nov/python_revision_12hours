# perfect number 6,28,496
num=int(input("enter a number ="))
sum_div=0
for i in range(1,num):
    if num%i==0:
        sum_div+=i
if sum_div==num:
    print(f"perfect number = {sum_div}")
else:
    print("not perfect number ")
    