# Demonstrates defining a function with a return value

def main():
    x = int(input("What's x? "))
    print("x squared is", squared(x))

def squared(n):
    return n * n

main()  