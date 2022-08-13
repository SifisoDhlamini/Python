import csv

students = []

name = input("Enter name: ")
home = input("Enter home: ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
# with open("students.csv") as file:
#      reader = csv.DictReader(file)
#      for row in reader:
#          students.append({"name": row["name"], "home": row["home"]})


# for student in sorted(students, key=lambda student: student["name"]):
#      print(f"{student['name']} is from {student['home']}")
