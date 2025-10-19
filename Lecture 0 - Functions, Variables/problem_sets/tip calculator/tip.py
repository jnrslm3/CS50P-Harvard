# This program calculates a tip for a meal.
# It asks the user for the cost of the meal and the tip percentage,
# then prints how much to leave.
def main() -> None:
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    d = float(d.replace("$", ""))
    return d

def percent_to_float(p: str) -> float:
    p = float(p.replace("%", ""))
    p /= 100
    return p

if __name__ == "__main__":
    main()