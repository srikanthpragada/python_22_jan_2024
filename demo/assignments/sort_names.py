
names = []
while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    names.append(name.upper())

names.sort()
print(names)


