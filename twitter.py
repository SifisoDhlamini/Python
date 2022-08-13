import re
url = input("Enter your twitter url: ").strip()

username = re.sub(r"^.+(https://twitter.com/)","@",url, re.IGNORECASE)
if matches := re.search(r"^(@[\w]+)+", username):
    print(f"Username: {matches.group(1)}")
