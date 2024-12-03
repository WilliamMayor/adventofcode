import re


def main():
    with open("q3/input.txt", "r") as fd:
        input_ = fd.read()
    total = 0
    for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_):
        total += int(a) * int(b)
    print(total)


if __name__ == "__main__":
    main()
