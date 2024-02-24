import os

gen = os.walk(r"d:\classroom\jan22p")
count = 0
for (dirname, folders, files) in gen:
    print(f"Directory : {dirname} ")
    for file in files:
        if file.endswith(".py"):
            print('  ', file)
            count += 1


print(f"Count = {count}")

