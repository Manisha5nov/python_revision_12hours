# product all digit of number 
num=int(input("enter a number = "))
mul=1
while num>0:
    r=num%10
    mul*=r
    num//=10
print(f"multipal of digit {mul}")
    
    