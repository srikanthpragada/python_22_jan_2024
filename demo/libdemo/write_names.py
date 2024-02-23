names = ['Larry', 'Jack', 'Scott', 'Steve', 'Mark', 'Joe']

with open("names.txt", "wt") as f:
    for n in names:
        f.write(n + "\n")



