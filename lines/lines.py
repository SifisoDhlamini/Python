import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("To few command-line arguments")

def main():
    lines = 0
    if(sys.argv[1].endswith(".py")):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if is_line(line):
                        lines+=1
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

    print(lines)


def is_line(line):
    if line.strip().startswith("#") or line.strip() == "":
        return False
    return True


if __name__ == "__main__":
  main()
