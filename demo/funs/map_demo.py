for n in map(abs, [-12, 10, 45, -34]):
    print(n)


def convert(s):
    if s.isdigit():
        return int(s)
    else:
        return 0


for n in map(convert, ["12", "45", "a4b5c", "r123"]):
    print(n)
