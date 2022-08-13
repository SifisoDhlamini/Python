def main():
    greeting = input("Enter your greeting: ").strip()
    print(f"${value(greeting)}")


def value(greeting):
    if(greeting.startswith("hello").lower()):
        return 0
    elif(greeting.startswith("h").lower()):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
