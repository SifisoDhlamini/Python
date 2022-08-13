def calcFraction(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).strip().split('/'))
        except ValueError:
            pass
        else:
            if x <= y & y > 0:
                return round((x/y) * 100)

def main():
    fraction = calcFraction("Fraction: ")
    if fraction <= 1:
        print('E')
    elif fraction >= 99:
        print('F')
    else:
        print(f"{fraction}%")


main()
