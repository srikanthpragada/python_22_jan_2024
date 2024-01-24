# Take price and display net price after a discount of 10%

data = input("Enter price :")
price = int(data)    # Convert str to int
discount = price * 10 // 100
net_price = price - discount
print('Net price =', net_price)



