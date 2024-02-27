import re

with open("gaza.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"[a-zA-Z]+", contents.upper())

for w in sorted(set(words)):
    if not w.isdigit():
        print(f"{w:15} {words.count(w):3}")
