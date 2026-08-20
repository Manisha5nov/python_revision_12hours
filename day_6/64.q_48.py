# even digit 
num=int(input("enter a number ="))
while num>0:
    r=num%10
    if r%2==0:
        print(f"even {r}")
    else :
        print(f"odd {r}")
    num//=10