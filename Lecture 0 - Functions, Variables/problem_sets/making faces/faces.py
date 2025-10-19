# This program converts text-based smiley faces into emoji equivalents.
def main():
    text = input("Please enter a sentence containing ':)' or ':(' to replace with emojis: ")
    print(convert(text))

def convert(faces):
    return faces.replace(":)", "🙂").replace(":(", "🙁")

main()