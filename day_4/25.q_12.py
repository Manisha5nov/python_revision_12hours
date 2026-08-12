pin=3333
pin1=int(input("enter your pin="))
pin=pin1
if pin==pin1:
    print("your pin is correct")
    print("Withdrawal amount and Check balance")
    wc=input("withdrawal for 'W' and check for 'C' =" )
    amount=10000
    if wc=="w" or wc=="W":
        print("withdrawal amount")
        amo=int(input("enter your amount ="))
        if amount>=amo:
            print(f"your current balance ={amount-amo}")
        else:
            print(f"your current balance low")
    elif wc=="c" or wc=="C":
        print(f"your current amount ={amount}")
else:
    print("your pin wrong")
