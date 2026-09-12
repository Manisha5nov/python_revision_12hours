# *********
# **      *   
# *   *   *
# **      *
# *********  print this pattern

n=int(input("Enter the number of rows: "))
for i in range(n):  
    
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i == j and i <= n//2) or (i+j == n-1 and i >= n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    