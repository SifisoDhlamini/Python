def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            print(guage(convert(fraction)))
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
    except ValueError:
        raise ValueError
    else:
        try:
            percentage =  round((x/y) * 100)
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            if x <= y:
                return percentage
            raise ValueError


def gauge(fraction):
    if fraction <= 1:
       return 'E'
    elif fraction >= 99:
        return 'F'
    else:
        return f"{fraction}%"


if __name__ == "__main__":
    main()
