import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    found = re.findall(r"^\W?(um)\W*|\W+(um)\W*", s, re.IGNORECASE)
    return len(found)


...


if __name__ == "__main__":
    main()
