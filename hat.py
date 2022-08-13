import random

# class Hat:
#     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     @classmethod
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))


# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     @property
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(name):
        print(name, "is in", random.choice(houses))


def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()