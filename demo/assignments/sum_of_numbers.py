
data = "90,78,ab,93,54"

total = 0
for v in data.split(","):
    total += int(v)

print(total)
