"""Find the number of unique positions that the guard moves through."""


def find_guard(map: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col == "^":
                return (row_idx, col_idx), (-1, 0)
    return (-1, -1), (0, 0)


def move_guard(
    map: list[str],
    position: tuple[int, int],
    direction: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int]]:
    row, col = position
    row_delta, col_delta = direction

    next_row = row + row_delta
    next_col = col + col_delta
    if next_row < 0 or next_col < 0:
        return (-1, -1), (0, 0)
    try:
        next_cell = map[next_row][next_col]
        if next_cell == "#":
            direction = {
                (-1, 0): (0, 1),
                (0, 1): (1, 0),
                (1, 0): (0, -1),
                (0, -1): (-1, 0),
            }[direction]
            return move_guard(map, position, direction)
        return (next_row, next_col), direction
    except IndexError:
        return (-1, -1), (0, 0)


def main():
    with open("q06/input.txt", "r") as fd:
        map: list[str] = fd.readlines()

    position, direction = find_guard(map)

    visited = set()
    while position != (-1, -1):
        visited.add(position)
        position, direction = move_guard(map, position, direction)

    print(len(visited))


if __name__ == "__main__":
    main()
