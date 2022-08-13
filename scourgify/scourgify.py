import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit(f"Could not read {sys.argv[1]}")

def main():
    try:
        students = read_file(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        write_to_file(sys.argv[2], students)


def read_file(arg):
    students = []
    with open(arg) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})
        return students


def write_to_file(arg, students):
    with open(arg, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            last, first = student["name"].split(",")
            writer.writerow({"first": first.lstrip(), "last": last, "house": student["house"]})


if __name__ == "__main__":
    main()

