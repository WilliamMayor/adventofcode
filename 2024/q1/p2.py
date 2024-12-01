from collections import Counter


def main():
    with open("q1/input.txt", "r") as fd:
        input_ = fd.read()
    parts = input_.split()
    first = [int(p) for p in parts[::2]]
    second = Counter(int(p) for p in parts[1::2])

    total = sum(f * second.get(f, 0) for f in first)
    print(total)


if __name__ == "__main__":
    main()
