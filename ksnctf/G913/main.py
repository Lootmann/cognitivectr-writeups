import math


def load(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    line = load(filename="./pi.txt")
    for i in range(len(line) - 10):
        num = int(line[i : i + 10])
        if is_prime(num):
            print(num)
            return


if __name__ == "__main__":
    main()
