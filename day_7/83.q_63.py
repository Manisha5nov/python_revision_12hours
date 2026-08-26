# even digit sum
n=int(input("enter a number = "))
eve=0
for i in range(1,n+1):
    if n>0:
        r=n%10
        if r%2==0:
            eve+=r
        n//=10
print(eve)
        