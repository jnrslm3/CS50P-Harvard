import re
import sys


def main() -> None:
    print(validate(input("IPv4 Address: ")))

def validate(ip) -> bool:
    nums = ip.split(".")
    if len(nums) != 4:
        return False

    for num in nums:
        if not num.isdigit():
            return False
        if len(num) > 1 and num.startswith("0"):
            return False
        if not 0 <= int(num) <= 255:
            return False

    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match = re.search(pattern, ip)
    return True if match else False


if __name__ == "__main__":
    main()