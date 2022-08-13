import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^<iframe.+(youtube.com/embed/)(\w+).+></iframe>$", s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(2)
    return None

if __name__ == "__main__":
    main()
