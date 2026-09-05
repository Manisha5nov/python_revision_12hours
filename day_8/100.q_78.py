# 1
# 21
# 321
# 4321   print the pattern

n=int(input("enter a number = "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()