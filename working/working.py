import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1]?[0-9]:?(?:[0-5][0-9])?) (\w\w) to ([1]?[0-9]:?(?:[0-5][0-9])?) (\w\w)$", s, re.IGNORECASE):
            if len(matches.group(1)) > 2:
                from_hrs, from_mins = matches.group(1).split(":")
            else:
                from_hrs = matches.group(1)
                from_mins = "00"


            if len(matches.group(3)) > 2:
                to_hrs, to_mins = matches.group(3).split(":")
            else:
                to_hrs = matches.group(3)
                to_mins = "00"


            if int(to_hrs) <= 12 and int(from_hrs) <= 12:
                from_period = matches.group(2)
                to_period = matches.group(4)

                if from_period.upper() == "PM" and int(from_hrs) < 12:
                    from_hrs = f"{int(from_hrs) + 12}"
                elif from_period.upper() == "AM" and int(from_hrs) == 12:
                    from_hrs = "00"

                if to_period.upper() == "PM" and int(to_hrs) < 12:
                    to_hrs = f"{int(to_hrs) + 12}"
                elif to_period.upper() == "AM" and int(to_hrs) == 12:
                    to_hrs = "00"

                return f"{int(from_hrs):02d}:{int(from_mins):02d} to {int(to_hrs):02d}:{int(to_mins):02d}"
            else:
                raise ValueError

    else:
        raise ValueError






if __name__ == "__main__":
    main()
