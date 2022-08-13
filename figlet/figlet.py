from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    index = random.randint(0, len(fonts) - 1)
    text = input("Input: ")
    figlet.setFont(font=fonts[index])
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        try:
            figlet.setFont(font=fonts[fonts.index(sys.argv[2])])
        except ValueError:
            sys.exit("Invalid usage")
        else:
           text = input("Input: ")
           print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
