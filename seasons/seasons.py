from datetime import date
import inflect
import sys


def main():
    p = inflect.engine()
    today = date.today()
    dob = DOB(input("Date of Birth: ").strip())
    difference = today - dob
    minutes = convert_min(difference)
    output = p.number_to_words(minutes, andword="")
    print(output.capitalize(), "minutes")


def DOB(dob):
    try:
        year, month, day = map(int, dob.split('-'))
    except:
        sys.exit("Invalid date")
    else:
        try:
            _dob = date(year, month, day)
        except:
            sys.exit("Invalid date")
        else:
            if _dob > date.today():
                sys.exit("Invalid date")
        return _dob


def convert_min(diff):
    return diff.days *24 * 60

if __name__ == "__main__":
    main()
