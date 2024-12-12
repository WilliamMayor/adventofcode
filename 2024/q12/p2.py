"""
Understanding
-------------
Now, instead of counting the size of perimiter you need to count the number of
sides of the region.

Notes
-----

I found this one complicated to think through, but not computationally
difficult.

I think the code could be tidied up here quite a bit.

The strategy is to find every cell in the region and also record on which side
the cell connects to a different region. Then group up all the sides that are
oriented in the same direction, and share either a row or column. Then find how
many contiguous stretches of sides there are. Each contiguous section is a
"side" from the point of view of the question, so count them all.

Day 12 - Time 16:13:03 - Rank 21289 - Score 0

Runs in 0.07s on my machine.
"""

import itertools
from collections.abc import Iterator

Location = tuple[int, int]
Direction = tuple[int, int]
Side = tuple[Direction, Location]
Area = tuple[str, int, set[Side]]

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def get_plant(input_: list[str], loc: Location) -> str | None:
    if loc[0] < 0 or loc[1] < 0:
        return
    try:
        return input_[loc[0]][loc[1]]
    except IndexError:
        pass


def explore(
    input_: list[str], loc: Location, plant: str, visited: set[Location]
) -> tuple[Area, set[Location]]:
    visited.add(loc)
    count: int = 1
    sides: set[Side] = set()
    for d in DIRECTIONS:
        next_loc: Location = (loc[0] + d[0], loc[1] + d[1])
        next_plant: str | None = get_plant(input_, next_loc)
        if next_plant == plant:
            if next_loc not in visited:
                (_, c, s), visited = explore(input_, next_loc, plant, visited)
                count += c
                sides.update(s)
        else:
            sides.add((d, loc))
    return (plant, count, sides), visited


def merge_locations(sides: Iterator[Side], axis: int) -> list[Side]:
    result = []
    start: Location | None = None
    stop: Location | None = None
    for side in sorted(sides, key=lambda side: side[1][axis]):
        loc = side[1]
        if stop is None:
            start, stop = loc, loc
        elif loc[axis] > stop[axis] + 1:
            result.append((start, stop))
            start, stop = loc, loc
        else:
            stop = loc
    result.append((start, stop))
    return result


def count_sides(sides: set[Side]) -> int:
    sorted_sides: list[Side] = sorted(sides, key=lambda s: s[0])
    by_dir = itertools.groupby(sorted_sides, lambda s: s[0])
    count = 0
    for dir, d_sides in by_dir:
        d_sides = list(d_sides)
        if dir[0] == 0:
            # Same row, side on left or right
            sorted_sides: list[Side] = sorted(d_sides, key=lambda s: s[1][1])
            for col, c_sides in itertools.groupby(sorted_sides, lambda s: s[1][1]):
                c_sides = merge_locations(c_sides, 0)
                count += len(c_sides)
        else:
            # Same col, side on top or bottom
            sorted_sides: list[Side] = sorted(d_sides, key=lambda s: s[1][0])
            for row, r_sides in itertools.groupby(sorted_sides, lambda s: s[1][0]):
                r_sides = merge_locations(r_sides, 1)
                count += len(r_sides)
    return count


def main():
    with open("q12/input.txt", "r") as fd:
        input_ = fd.read().strip().split("\n")

    total = 0
    visited = set()

    for row_idx, row in enumerate(input_):
        for col_idx, plant in enumerate(row):
            loc: Location = (row_idx, col_idx)
            if loc not in visited:
                (_, count, sides), visited = explore(input_, loc, plant, visited)
                side_count = count_sides(sides)
                total += count * side_count

    print(total)


if __name__ == "__main__":
    main()
