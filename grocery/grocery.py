grocery = {}
while True:
    try:
        item = input().strip()
    except EOFError:
        break
    else:
        if item.upper() in grocery:
            grocery[item.upper()] += 1
        else:
            grocery[item.upper()] = 1


for item in sorted(grocery):
    print(grocery[item], item)

