import re

name =input("What's your name: ")
if matches := re.search(r"^([a-z]+), *([a-z]+)$", name, re.IGNORECASE):
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")
