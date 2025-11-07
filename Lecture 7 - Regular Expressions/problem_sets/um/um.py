import re
import sys

def main() -> None:
    print(count(input("Text: ")))

def count(s) -> int:
    matches = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
