def main():
    with open("q1/input.txt", "r") as fd:
        input_ = fd.read()
    parts = input_.split()
    first = sorted([int(p) for p in parts[::2]])
    second = sorted([int(p) for p in parts[1::2]])

    total = sum(abs(f - s) for f, s in zip(first, second))
    print(total)


if __name__ == "__main__":
    main()
