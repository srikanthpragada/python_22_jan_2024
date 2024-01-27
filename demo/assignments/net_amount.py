# calculate net amount

qty = int(input("Enter qty :"))
price = int(input("Enter price : "))

amount = qty * price

if qty > 3:
    discount = amount * 20 // 100
else:
    discount = amount * 10 // 100

after_discount = amount - discount

print(f'Amount          : {amount:6}')
print(f'- Discount      : {discount:6}')
print(f'After Discount  : {after_discount:6}')

if after_discount > 10000:
    discount = after_discount * 5 // 100
    final_amount = after_discount - discount
    print(f"- Additional Discount : {discount:6}")
    print(f"Final Amount          : {final_amount:6}")
