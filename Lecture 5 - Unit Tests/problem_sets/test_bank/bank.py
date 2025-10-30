def main() -> None:
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


def value(g: str) -> int:
    g = g.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
