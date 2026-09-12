#         1
#     1   2   1
# 1   3   3   3   1   print this pettern
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        if k == 0 or k == 2*i:
            print("1", end="")
        else:
            print(i, end="")
    print()
    