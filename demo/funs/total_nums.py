data = "23,44,55,68,90,45"

total = 0
for v in data.split(","):
    total += int(v)

print(total)

print(sum(map(int, data.split(','))))
