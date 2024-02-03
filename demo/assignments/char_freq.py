
st = "how do you do"

# print char in dict order
for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")

# print char in the order they appear in the string
visited = []
for c in st:
    if c not in visited:
        print(f"{c} - {st.count(c)}")
        visited.append(c)
