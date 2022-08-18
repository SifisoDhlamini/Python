dist = int(input())
words = {}
for i in range(dist):
    word = input().strip()
    try:
        words[word] += 1
    except:
        words[word] = 1

print(len(words))
for word in words:
    print(words[word], end=" ")
