def is_safe(line):
    previous = line[0]
    is_increasing = None
    for current in line[1:]:
        if is_increasing is None:
            is_increasing = current > previous

        if is_increasing:
            if current <= previous:
                return False
            if current > previous + 3:
                return False
        else:
            if current >= previous:
                return False
            if current < previous - 3:
                return False

        previous = current
    return True


def is_safe_with_removals(line):
    line = list(map(int, line.split()))

    if is_safe(line):
        return True

    for idx in range(len(line)):
        smaller_line = list(line)
        smaller_line.pop(idx)
        if is_safe(smaller_line):
            return True
    return False


def main():
    with open("q02/input.txt", "r") as fd:
        input_ = fd.readlines()

    lines = filter(is_safe_with_removals, input_)

    total = len(list(lines))
    print(total)


if __name__ == "__main__":
    main()
