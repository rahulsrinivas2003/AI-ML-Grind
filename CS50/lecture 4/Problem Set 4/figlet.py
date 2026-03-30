import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    choice = random.choice(fonts)
    figlet.setFont(font=choice)

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

statement = input("Input: ")
print("Output: ", figlet.renderText(statement))
