"""
Understanding
-------------
The robots keep moving and at some point some of them line up to form a
christmas tree. What's the earliest they do this?

Notes
-----
This one was fun. You don't get any information about what the tree looks like,
but I figured that any picture of a christmas tree would involve lots of
diagonal lines. So I simply detected how often the robots are diagonally in a
line. If on a particular second more of them were in a diagonal than a threshold
I set then I'd print the layout of the robots and see if they looked like a
tree.

Rankings (my best yet):

Day 14 - Time 05:34:56 - Rank 11441 - Score 0

Runs in 0.93s on my machine (exlucing the time for the user to look at the
drawing and agree that it looks like a Christmas tree).
"""

import re

Position = tuple[int, int]
Velocity = tuple[int, int]

WIDTH = 101
HEIGHT = 103

RE_GUARD = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

ENDC = "\033[0m"
OKGREEN = "\033[92m"


def parse(guard: str) -> list:
    # p=0,4 v=3,-3
    match = re.match(RE_GUARD, guard)
    if match is None:
        raise Exception()
    return [(int(match[1]), int(match[2])), (int(match[3]), int(match[4]))]


def draw(positions: set[Position]):
    print("\033[H\033[J", end="")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in positions:
                print(f"{OKGREEN}#{ENDC}", end="")
            else:
                print(".", end="")
        print("")


def main():
    with open("q14/input.txt", "r") as fd:
        input_ = fd.read().strip().split("\n")

    guards = [parse(guard) for guard in input_]

    seconds = 0
    while True:
        seconds += 1
        likelihood = 0
        positions = set()
        for guard in guards:
            pos = (
                (guard[0][0] + guard[1][0]) % WIDTH,
                (guard[0][1] + guard[1][1]) % HEIGHT,
            )
            if (pos[0] - 1, pos[1] - 1) in positions or (
                pos[0] + 1,
                pos[1] + 1,
            ) in positions:
                likelihood += 1
            positions.add(pos)
            guard[0] = pos
        if likelihood > 100:
            draw(positions)
            print("Seconds", seconds)
            input()


if __name__ == "__main__":
    main()
