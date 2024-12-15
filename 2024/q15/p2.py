"""
Understanding
-------------

Everything on the map gets twice as wide, except the robot. This means that
pushing boxes is trickier, first because there are two chars that represent a
box ([ and ]) and you can't split them up, a secondly because one box could push
two other boxes in a V shape and if either branch of the V hit a wall then
neither branch can move.

Notes
-----

Went for a bit of recursion for this one. I found the rules quite complicated
and I worried that the runtime for this would be too big, that I would need
something fancier if I wanted the answer this century. Luckily, this one ran
in good time.

Rankings:

Day 15 - Time 16:52:02 - Rank 18274 - Score 0

Runs in 0.07s on my machine.
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


def push_boxes(
    map_: list[list[str]], pos: tuple[int, int], ins: str
) -> tuple[list[list[str]], tuple[int, int] | None]:
    dir = DIRECTIONS[ins]
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    next_cell = map_[next_pos[0]][next_pos[1]]

    if next_cell == ".":
        return map_, next_pos

    if next_cell == "#":
        return map_, None

    assert next_cell in ("[", "]")

    if ins in ("<", ">"):
        map_, second_pos = push_boxes(map_, next_pos, ins)
        if second_pos:
            map_[second_pos[0]][second_pos[1]] = next_cell
            return map_, next_pos
        return map_, None

    assert ins in ("^", "v")

    moved_map, second_pos_1 = push_boxes([list(line) for line in map_], next_pos, ins)
    if second_pos_1:
        other_cell = "]"
        other_pos = (next_pos[0], next_pos[1] + 1)
        if next_cell == "]":
            other_cell = "["
            other_pos = (next_pos[0], next_pos[1] - 1)
        moved_map, second_pos_2 = push_boxes(moved_map, other_pos, ins)
        if second_pos_2:
            moved_map[second_pos_1[0]][second_pos_1[1]] = next_cell
            moved_map[second_pos_2[0]][second_pos_2[1]] = other_cell
            moved_map[other_pos[0]][other_pos[1]] = "."
            return moved_map, next_pos
    return map_, None


def step(map_: list[list[str]], pos: tuple[int, int], cell: str, ins: str):
    map_, next_pos = push_boxes(map_, pos, ins)

    if next_pos:
        map_[pos[0]][pos[1]] = "."
        map_[next_pos[0]][next_pos[1]] = "@"
        return map_, next_pos

    return map_, pos


def enlarge_map(map_: list[list[str]]) -> list[list[str]]:
    new_map = []
    for row in map_:
        new_row = []
        new_map.append(new_row)
        for cell in row:
            if cell == "#":
                new_row.append("#")
                new_row.append("#")
            elif cell == "O":
                new_row.append("[")
                new_row.append("]")
            elif cell == ".":
                new_row.append(".")
                new_row.append(".")
            elif cell == "@":
                new_row.append("@")
                new_row.append(".")
    return new_map


def draw(map_, ins):
    print("\033[H\033[J", end="")
    for row in map_:
        for cell in row:
            if cell == "@":
                cell = f"\033[92m{cell}\033[0m"
            print(cell, end="")
        print("")
    print("")
    print(ins)


def main():
    with open("q15/input.txt", "r") as fd:
        map_, instructions = fd.read().strip().split("\n\n", 1)

    map_ = [list(line) for line in map_.split("\n")]
    instructions = instructions.replace("\n", "").strip()

    map_ = enlarge_map(map_)

    pos = find_robot(map_)

    for ins in instructions:
        # draw(map_, ins)
        # input()
        map_, pos = step(map_, pos, map_[pos[0]][pos[1]], ins)
    # draw(map_, ins="")

    total = 0
    for row_idx, row in enumerate(map_):
        for col_idx, cell in enumerate(row):
            if cell == "[":
                total += 100 * row_idx + col_idx
    print(total)


if __name__ == "__main__":
    main()
