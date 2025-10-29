import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0730baf3045de1175139d1db07d312016cd6739cdad2ed56f63b649ea78fb682")
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Network error")

    total = amount * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()