def main() -> None:
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if not ( 2 <= len(s) <= 6):
        return False
    else:
        if not s[:2].isalpha():
            return False
        else:
            if not s.isalnum():
                return False
            else:
                found_digit = False

                for ch in s:
                    if ch.isdigit():
                        if not found_digit:
                            if ch == '0':
                                return False 
                            found_digit = True
                    else:  
                        if found_digit:
                            return False  
                return True





if __name__ == "__main__":
    main()