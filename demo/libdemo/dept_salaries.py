
f = open("salaries.txt", "rt")

dept = {}

for line in f.readlines():
    try:
        parts = line.split(",")
        dname = parts[0]
        salary = int(parts[1])

        total = dept.get(dname, 0)
        dept[dname] = total + salary
    except Exception as ex:
        #print('Error :', ex)
        pass

f.close()

for dname, total in dept.items():
    print(f"{dname:10}  {total:6}")




