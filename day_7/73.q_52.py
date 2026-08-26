num=int(input("enter a number :"))
num1=str(num)
n=len(num1)
sum=0
for i in num1:
    sum=sum+int(i)**n
if sum==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")