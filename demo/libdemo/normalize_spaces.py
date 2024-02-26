import re

with open("test.txt", "rt") as f:
    contents = f.read()

# remove multiple spaces
newcontents = re.sub(r' +', ' ', contents)

# remove multiple new lines
newcontents = re.sub(r'\n+', '\n', newcontents)
# print(newcontents)

with open("test.txt", "wt") as f:
    f.write(newcontents)
