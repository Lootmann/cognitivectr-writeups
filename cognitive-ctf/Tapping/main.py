def conv() -> dict:
    morse = {}

    with open("./morse.txt", "r") as f:
        for line in f.readlines():
            s = line.strip().split()
            morse[s[1]] = s[0]

    return morse


def origin() -> list:
    with open("./origin.txt", "r") as f:
        return list(f.readline().split())


def main():
    morse_dict = conv()

    ans = []

    for ch in origin():
        if ch not in {"{", "}"}:
            ans.append(morse_dict[ch])
        else:
            ans.append(ch)

    print("".join(ans))


if __name__ == "__main__":
    main()
