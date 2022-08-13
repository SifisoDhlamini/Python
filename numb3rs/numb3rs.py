import re
import sys

#COMPLETE REGEX FOR IP ADRESS as per https://www.regextutorial.org/regex-for-ip-address-match.php
#( 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]? )\.( 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]? )\.(25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]?)\.(25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]?)

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    values = ip.split(".")
    try:
        return all(int(ele) >= 0 and int(ele) <= 255 and len(ele) <= 3 and len(ele) >= 1 for ele in values)
    except ValueError:
        return False


if __name__ == "__main__":
    main()
