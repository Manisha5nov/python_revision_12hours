# start and end by user 

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
i=start
while i <= end :
    print(i,end=" ")
    i+=1
print(f"\nThe numbers from {start} to {end} are printed successfully.")