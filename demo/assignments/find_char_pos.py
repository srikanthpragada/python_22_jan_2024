s1 = "python"
s2 = "ruby"

for c in s2:
    pos = s1.find(c)
    if pos != -1:
        print(pos)
        break
else:
    print(-1)


