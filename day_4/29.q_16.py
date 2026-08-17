# take a year as input and print whether it is leap year or not

year=int(input("enter year = "))
if year%400==0 or (year%4==0 and year%100!=0):
    print(f"{year} is leap year")
else :
    print(f"{year} is not leap year")