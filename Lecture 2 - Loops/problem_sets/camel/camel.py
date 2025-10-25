def main() -> None:
    camel_case = input("camelCase: ")
    print(to_snake_case(camel_case))

def to_snake_case(text: str) -> str:
    result = ""
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

if __name__ == "__main__":
    main()
