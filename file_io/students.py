students = []


with open("students.csv") as file:
    for row in file:
        name, house = row.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")

