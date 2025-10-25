def main() -> None:
    user_input = input("Input: ")
    text = ""
    for i in user_input:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            text += i
    
    print(f"Output: {text}")


if __name__ == "__main__":
    main()