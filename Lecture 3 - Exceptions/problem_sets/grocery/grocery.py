def main() -> None:
    grocery = {}
    while True:
        try: 
            item = input().lower().strip()
            grocery[item] = grocery.get(item, 0) + 1
        except EOFError:
            print()
            break

    
    for item in sorted(grocery):
        print(f"{grocery[item]} {item.upper()}")

if __name__ == "__main__":
    main()