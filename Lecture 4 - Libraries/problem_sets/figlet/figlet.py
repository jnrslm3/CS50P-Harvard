from pyfiglet import Figlet
import sys
import random

def main() -> None:
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        try:
            figlet.setFont(font=sys.argv[2])
        except Exception:
            sys.exit("Invalid font name")
    else:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    print(figlet.renderText(user_input))

        
if __name__ == "__main__":
    main()