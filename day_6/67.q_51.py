# find the smallest digit
num=int(input("enter a number = "))
s=9
while num>0:
    r=num%10
    if s>r:
        s=r
    num//=10
print(f"smallest digit is {s}")
