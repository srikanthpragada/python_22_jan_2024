
names = ['Andy', 'Steve', 'Scott', 'Jack', 'Mark']

chars = set() # Empty set

for n in names:
    chars = chars | set(n)

print(sorted(chars))


