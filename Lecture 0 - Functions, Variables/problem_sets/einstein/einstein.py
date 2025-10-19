# This program calculates energy using Einstein's formula E = mc^2.
# It takes mass (in kilograms) from the user and prints the energy in scientific notation.
def main() -> None:
    num = int(input("Enter a mass in kg to get 𝐸: "))
    print(f"𝐸: {formula(num)}")

def formula(n: int) -> int:
    return n * 300_000_000 ** 2

if __name__ == '__main__':
    main()