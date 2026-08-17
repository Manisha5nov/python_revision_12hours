# only even number product
num=int(input("enter a number = "))
mul=1
while num>0:
    r=num%10
    if r%2==0:
        mul*=r
    num//=10
print(f"multipaly of even digit {mul}")