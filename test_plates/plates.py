def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length > 6 or length < 2:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    first = None
    for char in s:
        if char.isdigit() and first == None:
            first = int(char)
        if first == 0 or (first != None and not char.isdigit()):
            return False
    return True


if __name__ == "__main__":
    main()
