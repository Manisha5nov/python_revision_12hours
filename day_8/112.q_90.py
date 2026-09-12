#             *
#          *  *
#       *  *  *
#  * *  *  *  *
#     * *  *
#       *  *  *
#          *  *
#             *     print this pattern

n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        if j == 0:
            print(" "*(n-i-1), end="")
        elif j == n-i-2:
            print(" "*(n-i-1), end="")
    for k in range(i+1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        if j == 0:
            print(" "*(i+1), end="")
        elif j == i:
            print(" "*(i+1), end="")
    for k in range(n-i-1):
        print("*", end=" ")
    print()