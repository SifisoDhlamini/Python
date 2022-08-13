def main():
    x = get_x()
    print(f"The square of {x} is {square(x)}", )

def square(n):
    return n * n

def get_x():
    return int(input("What is x? "))

if __name__ == "__main__":
    main()