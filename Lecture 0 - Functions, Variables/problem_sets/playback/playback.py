# This program replaces all spaces in a user's input with three dots (...).
def main():
    text = input("Enter text: ").replace(" ", "...")
    print(text)

main()