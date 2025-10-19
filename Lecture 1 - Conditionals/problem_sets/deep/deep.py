def main() -> None:
    text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    match text: 
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()