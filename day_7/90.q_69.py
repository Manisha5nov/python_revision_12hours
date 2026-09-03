# odd number sum
n=int(input("enter a number = "))
total=0
for i in range(1,n+1):
    if i%2!=0:
        total+=i
        print(i)
print(total) 