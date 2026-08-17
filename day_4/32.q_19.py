# profit and loss

purches_price=int(input("enter a purches price = "))
selling_price= int(input("enter a selling price = "))

if purches_price>selling_price:
    print({"loss": purches_price - selling_price})
elif selling_price>purches_price:
    print({"profit": selling_price - purches_price})
else:
    print("No profit, no loss")