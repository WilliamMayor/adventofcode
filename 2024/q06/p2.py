"""Find all the unique positions to place an obstacle that would cause the guard to loop."""

Position = tuple[int, int]
Direction = tuple[int, int]


def find_guard(map: list[str]) -> tuple[Position, Direction]:
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col == "^":
                return (row_idx, col_idx), (-1, 0)
    raise ValueError


def next_position(map: list[str], position: Position, direction: Direction) -> Position:
    row, col = position
    row_delta, col_delta = direction

    next_row = row + row_delta
    next_col = col + col_delta

    if next_row < 0 or next_col < 0:
        raise ValueError

    if next_row + 1 >= len(map) or next_col + 1 >= len(map[next_row]):
        raise ValueError

    return next_row, next_col


def next_direction(direction: Direction) -> Direction:
    return {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }[direction]


def move_guard(
    map: list[str],
    position: Position,
    direction: Direction,
    obstacle: Position | None = None,
) -> tuple[Position, Direction]:
    next_row, next_col = next_position(map, position, direction)
    next_cell = map[next_row][next_col]
    if next_cell == "#" or (next_row, next_col) == obstacle:
        return position, next_direction(direction)
    return (next_row, next_col), direction


def simulate_guard(
    map: list[str],
    position: Position,
    direction: Direction,
    obstacle: Position | None = None,
) -> tuple[set[tuple[Position, Direction]], bool]:
    visited = set()
    while True:
        try:
            visited.add((position, direction))
            position, direction = move_guard(map, position, direction, obstacle)
            if (position, direction) in visited:
                return visited, True
        except ValueError:
            return visited, False


def main():
    with open("q06/input.txt", "r") as fd:
        map: list[str] = fd.readlines()

    total = 0
    start_position, start_direction = find_guard(map)

    visited, _ = simulate_guard(
        map,
        start_position,
        start_direction,
        obstacle=None,
    )
    visited = {v[0] for v in visited}

    for pos in visited:
        if pos == start_position:
            continue
        _, did_loop = simulate_guard(
            map,
            start_position,
            start_direction,
            obstacle=pos,
        )
        if did_loop:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
