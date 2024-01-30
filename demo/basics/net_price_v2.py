# Take price and display net price after a discount based on price

price = int(input("Enter price :"))

if price > 5000:
    discount = price * 20 // 100
else:
    discount = price * 10 // 100

net_price = price - discount

print(f"Price       : {price:5}")
print(f"- Discount  : {discount:5}")
print(f"Net Price   : {net_price:5}")
