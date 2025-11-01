import sys

def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        count = 0
        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "":  # skip blank lines
                    continue
                if line.lstrip().startswith("#"):  # skip comments
                    continue
                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)

if __name__ == "__main__":
    main()