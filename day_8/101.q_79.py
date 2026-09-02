# 1234
# 123
# 12
# 1  print the pattern
n=int(input("enter a number = "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()