size_a = int(input())
a = set(map(int, input().split()))
size_b = int(input())
b = set(map(int, input().split()))
c = set(a) ^ set(b)
for val in sorted(c, reverse=False):
    print(val)
