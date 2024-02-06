
data = ["1,60", "1,80", "2,50", "3,88", "4,55", "2,67"]

students = {}

for entry in data:
    rollno, marks = entry.split(",")
    total = students.get(rollno, 0)
    total += int(marks)
    students[rollno] = total
    #print(students)

for rollno, total in students.items():
    print(f"{rollno:2} - {total:3}")




