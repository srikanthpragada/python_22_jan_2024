for n in map(abs, [-12, 10, 45, -34]):
    print(n)

for n in map(lambda v: int(v) if v.isdigit() else 0, ["12", "45", "a4b5c", "r123"]):
    print(n)
