# Take price and display net price after a discount of 10%

data = input("Enter price :")
price = int(data)  # Convert str to int
discount = price * 10 // 100
net_price = price - discount

print(f"Price       : {price:5}")
print(f"- Discount  : {discount:5}")
print(f"Net Price   : {net_price:5}")
