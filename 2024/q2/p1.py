def is_safe(line):
    line = line.split()
    previous = int(line[0])
    is_increasing = None
    for current in line[1:]:
        current = int(current)

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


def main():
    with open("q2/input.txt", "r") as fd:
        input_ = fd.readlines()

    lines = filter(is_safe, input_)

    total = len(list(lines))
    print(total)


if __name__ == "__main__":
    main()
