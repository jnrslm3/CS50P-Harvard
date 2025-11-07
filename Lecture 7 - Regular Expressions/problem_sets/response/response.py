import validators


def main() -> None:
    print(check_email(input("Enter an email: ")))

def check_email(s) -> str:
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()