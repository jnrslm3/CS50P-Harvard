def main() -> None:
    print_square(3)


def print_square(size: int) -> None:
    for _ in range(size):
        print_row(size)


def print_row(width: int) -> None:
    print("#" * width)

if __name__ == "__main__":
    main()