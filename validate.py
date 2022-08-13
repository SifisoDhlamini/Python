#re.search(pattern, string, flags=0)
import re

email = input("What's your email? ").strip()

if re.search(r"^[\w\.]+@[\w\.]+\.[a-z]+$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
