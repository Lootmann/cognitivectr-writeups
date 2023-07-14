def load(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


def rot(ch: str, diff: int = 0):
    if ch in {" ", ",", "."}:
        return ch

    if ch.islower():
        return chr((ord(ch) - ord("a") + diff) % 26 + ord("a"))
    else:
        return chr((ord(ch) - ord("A") + diff) % 26 + ord("A"))


def conv(origin: str, diff: int):
    ans = []

    for ch in origin:
        ans.append(rot(ch, diff))

    return "".join(ans)


def main():
    origin = load("./origin.txt")
    ans = []

    for diff in range(26):
        ans = conv(origin, diff)
        print(diff, ans)
        print()


if __name__ == "__main__":
    main()
