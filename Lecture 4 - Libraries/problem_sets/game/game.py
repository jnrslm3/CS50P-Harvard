import random

def main() -> None:
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0:
                break
        except ValueError:
            pass

        
    n = random.randint(1, lvl)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass
        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()