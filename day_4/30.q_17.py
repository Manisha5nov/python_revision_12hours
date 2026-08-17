# take a number as input .ptint second largest number from three numbers

num1=int(input("enter first number ="))
num2=int(input("enter second number ="))
num3=int(input("enter third number ="))
if num1>num2 and num1>num3:
    print(f"{num1} is greter")
    if num2>num3:
        print(f"{num2} is second greter")
    else:
        print(f"{num3} is second greter")
if num2>num1 and num2>num3:
    print(f"{num2} is greter")
    if num1>num3:
        print(f"{num1} is second greter")
    else:
        print(f"{num3} is second greter")
if num3>num2 and num3>num1:
    print(f"{num3} is greter")
    if num2>num1:
        print(f"{num2} is second greter")
    else:
        print(f"{num1} is second greter")
# elif num1==num2:
#     print(f"{num1} and {num2} are equle")
# elif num2==num3:
#     print(f"{num2} and {num3} are equle")
# elif num1==num3:
#     print(f"{num1} and {num3} are equle")
else :
    print(f"{num1},{num2},{num3} are equle")

