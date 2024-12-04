def build_mover(row_delta, col_delta):
    def move(input_, row_idx, col_idx, letters):
        if len(letters) == 0:
            return True

        new_row_idx = row_idx + row_delta
        if new_row_idx < 0 or len(input_) == row_idx + row_delta:
            return False

        new_col_idx = col_idx + col_delta
        if new_col_idx < 0 or len(input_[new_row_idx]) == new_col_idx:
            return False

        if input_[new_row_idx][new_col_idx] == letters[0]:
            return move(input_, new_row_idx, new_col_idx, letters[1:])
        return False

    return move


DIRECTIONS = [
    build_mover(-1, -1),
    build_mover(-1, 0),
    build_mover(-1, 1),
    build_mover(0, -1),
    build_mover(0, 1),
    build_mover(1, -1),
    build_mover(1, 0),
    build_mover(1, 1),
]


def main():
    with open("q4/input.txt", "r") as fd:
        input_ = fd.readlines()

        total = 0
        for row_idx, row in enumerate(input_):
            for col_idx, char in enumerate(row):
                if char == "X":
                    for d in DIRECTIONS:
                        if d(input_, row_idx, col_idx, ["M", "A", "S"]):
                            total += 1
        print(total)


if __name__ == "__main__":
    main()
