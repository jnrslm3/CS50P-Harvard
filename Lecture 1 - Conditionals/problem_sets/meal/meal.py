def main() -> None:
    time = input("What time is it? ")
    convert(time)

def convert(time: str) -> None:
    hours, minutes = map(int, time.split(":"))
    time_decimal = hours + minutes / 60

    if 7 <= time_decimal <= 8.5: 
        print("breakfast time")
    elif 12 <= time_decimal <= 13: 
        print("lunch time")
    elif 18 <= time_decimal <= 19: 
        print("dinner time")
    else:
        print("Not meal time")

if __name__ == "__main__":
    main()
