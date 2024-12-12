"""
Understanding
-------------
The input is a map showing different regions. The task is to find the area and
perimeter of each region.

Notes
-----

This one was fun. Nice little recursive function to explore the map and find
every cell in the region.

Instead of trying to count the outermost edges of each region I:

    - Recursively found every cell in a region counting up the number of unique
    cells and the number of "links" between them (the number of times cells
    touched) within a region.
    - The perimeter of the region is then 4 times the area (i.e. a perimeter for
    each side of the cell) minus 2 times the number of links (i.e. the number of
    times the perimeter was on the inside of the region).

Not bad rankings:

Day 12 - Time 06:32:24 - Rank 19626 - Score 0

Runs in 0.03s on my machine.
"""

Location = tuple[int, int]
Area = tuple[str, int, int]

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def get_plant(input_, loc):
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
    count = 1
    links = 0
    for d in DIRECTIONS:
        next_loc = (loc[0] + d[0], loc[1] + d[1])
        next_plant = get_plant(input_, next_loc)
        if next_plant == plant:
            links += 1
            if next_loc not in visited:
                (_, c, l), visited = explore(input_, next_loc, plant, visited)
                count += c
                links += l
    return (plant, count, links), visited


def main():
    with open("q12/input.txt", "r") as fd:
        input_ = fd.read().strip().split("\n")

    total = 0
    visited = set()

    for row_idx, row in enumerate(input_):
        for col_idx, plant in enumerate(row):
            loc: Location = (row_idx, col_idx)
            if loc not in visited:
                (_, count, links), visited = explore(input_, loc, plant, visited)
                links = links // 2
                total += count * (4 * count - 2 * links)

    print(total)


if __name__ == "__main__":
    main()
