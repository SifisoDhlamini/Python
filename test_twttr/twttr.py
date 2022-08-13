vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

def main():
    word = input("Enter a word: ")
    print(shorten(word))


def shorten(word):
    twttr = ""
    for letter in word:
        if letter not in vowels:
            twttr += letter
    return twttr


if __name__ == "__main__":
    main()
