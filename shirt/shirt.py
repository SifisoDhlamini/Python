import sys
from PIL import Image, ImageOps

suffixes = ('jpg', 'png', 'jpeg')
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(suffixes) :
    sys.exit(f"Invalid intput")
if not sys.argv[2].endswith(suffixes):
    sys.exit(f"Invalid output")
if sys.argv[1][sys.argv[1].index("."):] != sys.argv[2][sys.argv[2].index("."):]:
    sys.exit("Input and output have different extensions")


image1 = Image.open(sys.argv[1])
image2 = sys.argv[2]
shirt = Image.open("shirt.png")
resized_image = ImageOps.fit(image1, size = shirt.size)
resized_image.paste(shirt, shirt)
resized_image.save(image2)










