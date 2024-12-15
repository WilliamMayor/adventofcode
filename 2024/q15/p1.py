"""
Understanding
-------------
A robot moves about in a grid according to a set of instructions. If it
encounters an O char then it can push it along in a straight line. If it
encounters a # then it can't move in that direction any further.

Execute all of the instructions and then locate each of the Os in the grid.

Notes
-----
Pretty fun, nice to make a draw function to see the robot moving around.

I just simulated the robot for this one, nothing fancy. When the robot hits an
O I just move along in a straight line looking for a free space. If I find one
then we can move the boxes along.

Rankings:

Day 15 - Time 05:00:00 - Rank 12582 - Score 0

Runs in 0.03s on my machine.
"""

DIRECTIONS = {
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
}


def find_robot(map_: list[list[str]]) -> tuple[int, int]:
    for row_idx, row in enumerate(map_):
        for col_idx, cell in enumerate(row):
            if cell == "@":
                return row_idx, col_idx
    return 0, 0


def step(map_: list[list[str]], pos: tuple[int, int], ins: str):
    dir = DIRECTIONS[ins]
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    next_cell = map_[next_pos[0]][next_pos[1]]

    if next_cell == ".":
        map_[pos[0]][pos[1]] = "."
        map_[next_pos[0]][next_pos[1]] = "@"
        return map_, next_pos

    if next_cell == "#":
        return map_, pos

    assert next_cell == "O"

    free_pos, free_cell = next_pos, "O"
    while free_cell == "O":
        free_pos = (free_pos[0] + dir[0], free_pos[1] + dir[1])
        free_cell = map_[free_pos[0]][free_pos[1]]

    if free_cell == "#":
        return map_, pos

    assert free_cell == "."
    map_[pos[0]][pos[1]] = "."
    map_[next_pos[0]][next_pos[1]] = "@"
    map_[free_pos[0]][free_pos[1]] = "O"
    return map_, next_pos


def draw(map_, ins):
    print("\033[H\033[J", end="")
    for row in map_:
        for cell in row:
            print(cell, end="")
        print("")
    print("")
    print(ins)


def main():
    with open("q15/input.txt", "r") as fd:
        map_, instructions = fd.read().strip().split("\n\n", 1)

    map_ = [list(line) for line in map_.split("\n")]
    instructions = instructions.replace("\n", "").strip()

    pos = find_robot(map_)

    for ins in instructions:
        map_, pos = step(map_, pos, ins)
    # draw(map_, ins="")

    total = 0
    for row_idx, row in enumerate(map_):
        for col_idx, cell in enumerate(row):
            if cell == "O":
                total += 100 * row_idx + col_idx
    print(total)


if __name__ == "__main__":
    main()
