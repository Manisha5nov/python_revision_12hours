# 1 to 100prime number :

num=int(input("enter a number "))
while num>0:
    c=0
    for i in range(2,num):
        if num%i==0:
            c+=1
            break
    if c==0:
        print(f"{num} is prime number ")
    num-=1