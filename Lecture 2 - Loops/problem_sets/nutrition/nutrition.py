def main() -> None:
    item = input("Item: ").lower()
    check_calories(item)


def check_calories(item: str) -> None:
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "grapefruit": 60,
        "grapes": 90,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    if item in fruits:  
        print(f"Calories: {fruits[item]}")


if __name__ == "__main__":
    main()