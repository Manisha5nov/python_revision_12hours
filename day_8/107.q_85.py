#         1
#     2   2   2
# 3   3   3   3   3   print this pettern
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print(i+1, end="")
    print()