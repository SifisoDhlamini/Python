names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
      #for line in sorted(file):
        #print("Hello,", line.rstrip())

for name in sorted(names, reverse=True):
   print(f"hello, {name}")
