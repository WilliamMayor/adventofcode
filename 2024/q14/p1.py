"""
Understanding
-------------
Some robots move around an area in a straight line, when they reach the edge of
the map, they appear on the other side (continuing in that straight line).

Simulate the guards moving for 100 seconds and see where they end up. Count all
of the robots in each quadrant of the map, and then multiply the counts
together.

Notes
-----
This was pretty easy, you know how far each robots goes in each direction per
second, simply multiply that distance by 100 to see how far they'd go in 100
seconds. Then modulo that number by the width or height (depending on which
direction you're adding up) to account for the robot appearing on the other
side of the map.

I'm sure there's a better way to work out what quadrant the robot is in. But
this version is fast enough so I'll leave it as it is.

Rankings (my best yet):

Day 14 - Time 05:10:43 - Rank 14796 - Score 0

Runs in 0.02s on my machine.
"""

from functools import reduce
import re

Position = tuple[int, int]
Velocity = tuple[int, int]

WIDTH = 101
HEIGHT = 103

RE_GUARD = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"


def parse(guard: str) -> tuple[Position, Velocity] | tuple[None, None]:
    # p=0,4 v=3,-3
    match = re.match(RE_GUARD, guard)
    if match is None:
        return None, None
    return (int(match[1]), int(match[2])), (int(match[3]), int(match[4]))


def which_quadrant(pos: Position) -> int:
    half_width = WIDTH // 2
    half_height = HEIGHT // 2
    if pos[0] == half_width or pos[1] == half_height:
        return 4
    if pos[0] < half_width:
        if pos[1] < half_height:
            return 0
        return 1
    if pos[1] < half_height:
        return 2
    return 3


def main():
    with open("q14/input.txt", "r") as fd:
        input_ = fd.read().strip().split("\n")

    quadrant_counts = [0, 0, 0, 0, 0]
    for guard in input_:
        pos, vel = parse(guard)
        assert pos is not None
        assert vel is not None

        future_pos = ((pos[0] + vel[0] * 100) % WIDTH, (pos[1] + vel[1] * 100) % HEIGHT)
        quadrant_counts[which_quadrant(future_pos)] += 1

    print(reduce(lambda a, b: a * b, quadrant_counts[:-1]))


if __name__ == "__main__":
    main()
