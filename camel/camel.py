camel = input("Variable: ")

snake = ""

for letter in camel:
    if letter.isupper():
        snake += f"_{letter.lower()}"
    else:
        snake += letter

print(snake)