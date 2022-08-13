students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def is_gryffindor(student):
    return student["house"] == "Gryffindor"


# gryffindors = list(filter(is_gryffindor, students))
gryffindors = list(filter(lambda student: student["house"] == "Gryffindor", students))
print(type(gryffindors))

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor["name"])

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# print(*gryffindors)

# def main():
#     yell("This", "is", "CS50")


# def yell(*words):
#     upeprcased = [word.upper() for word in words]
#     print(*upeprcased)


# if __name__ == "__main__":
#     main()
