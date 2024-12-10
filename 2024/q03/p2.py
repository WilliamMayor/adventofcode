import re


def main():
    with open("q03/input.txt", "r") as fd:
        input_ = fd.read()
    is_do = True
    total = 0
    for match in re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", input_):
        if match[0] == "do()":
            is_do = True
        elif match[0] == "don't()":
            is_do = False
        elif is_do:
            total += int(match[1]) * int(match[2])
    print(total)


if __name__ == "__main__":
    main()
