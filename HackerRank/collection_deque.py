from collections import deque

q = int(input())
d = deque()
for i in range(q):
    query = input()
    if len(query.split()) == 1:
        if query == "pop":
            d.pop()
        else:
            d.popleft()
    else:
        method, val = query.split()
        if method == "append":
            d.append(int(val))
        else:
            d.appendleft(int(val))

for value in d:
    print(value, end=" ")