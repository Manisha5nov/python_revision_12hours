# palindrom number

num=int(input("enter a number = "))
n=num
p=0
a=n%10
p=a*100
n//=10
a=n%10
p+=a*10
n//=10
p+=n
if num==p:
    print("palindrom")
else:
    print("not palindrom")