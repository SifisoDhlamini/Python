def main():
    x = getInt("What is x? ")
    print(f"x is {x}")

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #print("x is not an integer")
            pass

main()
