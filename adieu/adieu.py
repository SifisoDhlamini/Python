names = []
while(True):
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

length = len(names)
if length == 1:
    print(f"Adieu, adieu, to {names[0]}")
else:
    for i in range(length):
        if i == 0:
            print(f"Adieu, adieu, to {names[i]}", end="")
        elif length == 2:
            print(f" and {names[i]}")
        elif i == length - 1:
            print(f", and {names[i]}")
        else:
            print(f", {names[i]}", end="")

