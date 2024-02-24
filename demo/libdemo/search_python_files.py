import os


def contains_string(filename, search_string):
    with open(filename, "rt") as f:
        return search_string in f.read()


search = input("Enter search string :")
gen = os.walk(r"d:\classroom\jan22p\demo")

for (dirname, folders, files) in gen:
    for file in files:
        filename = dirname + "\\" + file
        if filename.endswith(".py"):
            if contains_string(filename, search):
                print(filename)
