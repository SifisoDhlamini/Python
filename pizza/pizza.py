import csv
import sys
from tabulate import tabulate
#print(tabulate(table, headers, tablefmt="grid"))

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

table = []
#fieldnames=["Regular Pizza", "Large", "Small"]
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append([row[0], row[1], row[2]])

except FileNotFoundError:
    sys.exit("File does not exist")


titles = table[0]
table.pop(0)
print(tabulate(table, headers = [titles[0], titles[1], titles[2]], tablefmt="grid"))



