import itertools


def main():
    with open("q07/input.txt", "r") as fd:
        input_ = fd.readlines()

    equations = []
    for line in input_:
        parts = line.strip().split(": ", 1)
        equations.append((int(parts[0]), list(map(int, parts[1].split(" ")))))

    total = 0
    for answer, numbers in equations:
        for operators in itertools.product("*+", repeat=len(numbers) - 1):
            attempt = 0
            op = "+"
            for n, next_op in itertools.zip_longest(numbers, operators):
                if op == "+":
                    attempt += n
                elif op == "*":
                    attempt *= n
                op = next_op
            if attempt == answer:
                total += answer
                break

    print(total)


if __name__ == "__main__":
    main()
