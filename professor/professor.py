import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0
        while(True):
            attempts += 1
            try:
                attempt = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if attempts == 3:
                    print((f"{x} + {y} = {answer}"))
                    break
            else:
                if attempt == answer:
                    score += 1
                    attempts = 0
                    break
                else:
                    print("EEE")

                if attempts == 3:
                    print((f"{x} + {y} = {answer}"))
                    break

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    while(True):
        if level == 1:
            return random.randint(0, 9)
        if level == 2:
            return random.randint(10, 99)
        if level == 3:
            return random.randint(100, 999)
        raise ValueError


if __name__ == "__main__":
    main()
