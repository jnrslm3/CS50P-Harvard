import emoji

def main() -> None:
    user_input = input("Input: ")
    print(f"Output: {emoji.emojize(user_input)}")


if __name__ == "__main__":
    main()