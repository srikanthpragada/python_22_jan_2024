import re

f = open("customers.txt", "rt")

for line in f:
    m = re.search(r"\d+", line)
    if m is not None:
        mobile = m.group()
        if len(mobile) == 10:
            print(mobile)

f.close()
