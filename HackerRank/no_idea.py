n, m = map(int, input().split())
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for elem in arr:
    if elem in a:
        happiness += 1
    if elem in b:
        happiness -= 1
print(happiness)