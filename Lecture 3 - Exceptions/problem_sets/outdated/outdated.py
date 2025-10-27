def main() -> None:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        user_input = input("Date: ").strip()
        try:
            m, d, y = user_input.split("/")
            if not (1 <= int(m) <= 12 and 1 <= int(d) <= 31):
                continue
            print(f"{int(y)}-{int(m):02}-{int(d):02}")
            break
        except ValueError:
            try:
                m, d, y = [x.strip() for x in user_input.split(" ")]
                if "," not in d:
                    continue
                d = d[:-1]
                if m in months and 1 <= int(d) <= 31:
                    print(f"{int(y)}-{months.index(m)+1:02}-{int(d):02}")
                    break
            except ValueError:
                continue

if __name__ == "__main__":
    main()
