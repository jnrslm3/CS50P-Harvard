def main() -> None:
    meow(get_number())


def get_number() -> int:
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

if __name__ == "__main__":
    main()