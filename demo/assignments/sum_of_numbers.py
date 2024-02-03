
data = "90,78,ab,93,54"

total = 0
for v in data.split(","):
    if v.isdigit():
        total += int(v)

print(total)
