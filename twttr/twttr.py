vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
word = input("Enter a word: ")
twttr = ""

for letter in word:
    if letter not in vowels:
        twttr += letter

print(twttr)


