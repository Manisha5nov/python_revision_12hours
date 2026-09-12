# *
# **
# ***
# ****
# ***
# **
# *     print this pattern

n=int(input("Enter the number of rows: "))
for i in range(n*2):
    for j in range(n+1):
        if i < n:
            if j <= i:
                print("*", end=" ")
        else:
            if j < (2*n-i):
                print("*", end=" ")
    print()