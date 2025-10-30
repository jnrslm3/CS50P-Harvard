def main() -> None:
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")

    
def shorten(word: str) -> str:
    text = ""
    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            text += i
    
    return text


if __name__ == "__main__":
    main()