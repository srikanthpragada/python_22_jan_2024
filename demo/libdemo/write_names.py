names = ['Larry', 'Jack', 'Scott', 'Steve', 'Mark', 'Joe']

f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()

