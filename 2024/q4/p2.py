def get_char(input_, row_idx, col_idx):
    if row_idx < 0 or col_idx < 0:
        return None
    try:
        return input_[row_idx][col_idx]
    except IndexError:
        return None


def check_mas(input_, a_row, a_col):
    nw = get_char(input_, a_row - 1, a_col - 1)
    se = get_char(input_, a_row + 1, a_col + 1)
    if (nw, se) == ("M", "S") or (nw, se) == ("S", "M"):
        ne = get_char(input_, a_row - 1, a_col + 1)
        sw = get_char(input_, a_row + 1, a_col - 1)
        return (ne, sw) == ("M", "S") or (ne, sw) == ("S", "M")
    return False


def main():
    with open("q4/input.txt", "r") as fd:
        input_ = fd.readlines()

        total = 0
        for row_idx, row in enumerate(input_):
            for col_idx, char in enumerate(row):
                if char == "A":
                    if check_mas(input_, row_idx, col_idx):
                        total += 1

        print(total)


if __name__ == "__main__":
    main()
