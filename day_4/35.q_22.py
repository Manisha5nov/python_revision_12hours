# armstrong number 

num=int(input("enter a number = "))
n=num
sum=0
a=n%10
sum+=a**3
n//=10
a=n%10
sum+=a**3
n//=10
sum+=n**3
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")
