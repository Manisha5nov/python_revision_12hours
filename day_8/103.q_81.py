for i in range(6,0,-1):
    for j in range(1,i):
        print("  ",end="  ")
    for k in range(6,i-1,-1):
        print(k,end="")    
    print()