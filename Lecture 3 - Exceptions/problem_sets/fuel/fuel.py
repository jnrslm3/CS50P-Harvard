def main() -> None:
    while True:
        fraction = input('Fraction: ')
        try: 
            a, b = fraction.split("/")
            a, b = int(a), int(b)
            if a > b:
                continue
            result = round((a/b) * 100)
            if result >= 99:
                print("F")
            elif result <= 1:
                print("E")
            else:
                print(f"{result}%")
            break
        except (ValueError, ZeroDivisionError):
            continue
        
    
if __name__ == "__main__":
    main()