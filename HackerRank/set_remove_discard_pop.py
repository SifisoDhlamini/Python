n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    operation = input()
    if operation.startswith('pop'):
        try:
            s.pop()
        except KeyError:
            continue
    else:
        func, val = operation.split()
        if func == 'remove':
            try:
                s.remove(int(val))
            except KeyError:
                continue
        else:
            s.discard(int(val))
print(sum(s))
