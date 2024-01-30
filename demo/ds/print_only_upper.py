name = input("Enter your name :")

for c in name:
    if ord(c) >= 65 and ord(c) <= 90:
        print(c, end='')

for c in name:
    if c.isupper():
        print(c, end='')
