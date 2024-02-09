names = ["Joe", "Steve", "Mark", "Mike", "Adams"]


def bigname(n):
    return len(n) > 4


def starts_with_m(n):
    return n.startswith('M')


for n in filter(bigname, names):
    print(n)

for n in filter(starts_with_m, names):
    print(n)
