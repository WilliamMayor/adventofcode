"""
Understanding
-------------

The input is a map, the number in each cell shows the height of the ground at
that location. You start at all locations at height 0 and the challenge is to
see how many height 9 cells you can reach by travelling up, right, down, or left
increasing the height by one at each step.

The answer is the total number of routes you can take from a 0 height
starting position that end at a 9 height position.

Notes
-----

Easier than part one? You don't have to track which nodes you've been to
already, you just have to make sure that you're not repeating routes.

Not bad ranking:

Day 10 - Time 10:16:21 - Rank 28103 - Score 0

Runs in 0.04s on my machine.
"""

from collections.abc import Iterator

Position = tuple[int, int]

DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]


def find_adjacent_cells(
    height_map: list[list[int]], position: Position
) -> Iterator[tuple[Position, int]]:
    for d in DIRECTIONS:
        next_position = (position[0] + d[0], position[1] + d[1])
        if next_position[0] >= 0 and next_position[1] >= 0:
            try:
                height = height_map[next_position[0]][next_position[1]]
                yield next_position, height
            except IndexError:
                pass


def find_paths(
    height_map: list[list[int]], position: Position, height: int
) -> Iterator[int]:
    if height == 9:
        yield 1
    else:
        for adj_position, adj_height in find_adjacent_cells(height_map, position):
            if height + 1 == adj_height:
                yield from find_paths(height_map, adj_position, adj_height)


def main():
    with open("q10/input.txt", "r") as fd:
        input_ = fd.read().strip().split()
    input_ = [list(map(int, line)) for line in input_]

    total = 0
    for row_idx, row in enumerate(input_):
        for col_idx, height in enumerate(row):
            if height == 0:
                position: Position = (row_idx, col_idx)
                total += sum(find_paths(input_, position, height))

    print(total)


if __name__ == "__main__":
    main()
