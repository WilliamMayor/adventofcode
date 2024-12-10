"""
Understanding
-------------

The input is a map, the number in each cell shows the height of the ground at
that location. You start at all locations at height 0 and the challenge is to
see how many height 9 cells you can reach by travelling up, right, down, or left
increasing the height by one at each step.

The answer is the sum of the number of unique 9s you can reach from each 0
height starting point.

Notes
-----

This one wasn't too tricky. I loop through the input looking for starting
positions and from each one explore the adjacent cells to see if they are the
correct next height. To keep things fast I keep a record of the positions we've
already visited, because if we've already been to a position then we'll only
ever end up at the same destinations, that we've already counted.

Not bad ranking:

Day 10 - Time 03:58:38 - Rank 17116 - Score 0

Runs in 0.02s on my machine.

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
    height_map: list[list[int]],
    position: Position,
    height: int,
    visited_cells: set[Position],
) -> Iterator[Position]:
    visited_cells.add(position)
    if height == 9:
        yield position
    else:
        for adj_position, adj_height in find_adjacent_cells(height_map, position):
            if adj_position in visited_cells:
                continue
            if height + 1 == adj_height:
                yield from find_paths(
                    height_map, adj_position, adj_height, visited_cells
                )


def main():
    with open("q10/input.txt", "r") as fd:
        input_ = fd.read().strip().split()
    input_ = [list(map(int, line)) for line in input_]

    total = 0
    for row_idx, row in enumerate(input_):
        for col_idx, height in enumerate(row):
            if height == 0:
                position: Position = (row_idx, col_idx)
                total += len(list(find_paths(input_, position, height, set())))

    print(total)


if __name__ == "__main__":
    main()
