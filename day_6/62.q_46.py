# largest digit 
num=int(input("enter a number = "))
s=0
while num>0:
    r=num%10
    if s<r:
        s=r
    num//=10

print(f"largest num {s}")