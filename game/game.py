import random
import sys

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level > 0:
            lucky = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    pass
                else:
                    if guess > 0:
                        if guess == lucky:
                            sys.exit("Just right!")
                        if guess < lucky:
                            print("Too small!")
                        if guess > lucky:
                            print("Too large!")


