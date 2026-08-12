print("WeLlCoMe My Restorent 'Codder'")
print("1.= Burgur (100)")
print("2.= Chowmin (50)")
print("3.= samosha (25)")
print("4.= momo (80)")

order=int(input("enter your order no ="))
if order==1:
    qut=int(input("enter your quintity ="))
    amount=qut*100
    print(f"your total amount ={amount}")
    print("Thanks for visit my restorent")

if order==2:
    qut=int(input("enter your quintity ="))
    amount=qut*50
    print(f"your total amount ={amount}")
    print("Thanks for visit my restorent")

if order==4:
    qut=int(input("enter your quintity ="))
    amount=qut*80
    print(f"your total amount ={amount}")
    print("Thanks for visit my restorent")
