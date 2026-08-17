# a shope gives discount based on purchase amount
# above 5000-20% discount
# above 2000-10% discount
# above 1000-5% discount
# 1000 or below - no discount

amount=int(input("enter your amount ="))
if amount>=5000:
    discount=amount*20/100
elif amount>=2000:
    discount=amount*10/100
elif amount>=1000:
    discount=amount*5/100
else :
    print(f"{amount} no discount ")
final_amount=amount-discount
print(f"your discount = {discount}")
print(f"your final_amount = {final_amount}")