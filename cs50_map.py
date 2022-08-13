def main():
    yell("This", "is", "CS50")

def yell(*words):
    upeprcased = map(str.upper, words)
    print(*upeprcased)

if __name__ == "__main__":
    main()

