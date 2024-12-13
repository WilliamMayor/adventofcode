"""
Understanding
-------------
Solve some simultaneous equations!

Notes
-----
I had to look up how to do this computationally, I could just about remember how
to do it by hand. I found this guide:

https://www.mathcentre.ac.uk/resources/Engineering%20maths%20first%20aid%20kit/latexsource%20and%20diagrams/5_6.pdf

Rankings:

Day 13 - Time 15:18:20 - Rank 24493 - Score 0

Runs in 0.02s on my machine.
"""

import re
from collections import namedtuple

RE_BUTTON = r"Button [AB]: X\+(\d+), Y\+(\d+)"
RE_PRIZE = r"Prize: X=(\d+), Y=(\d+)"

XY = namedtuple("XY", "x,y")
Machine = namedtuple("Machine", "a,b,prize")


def parse(m):
    a, b, p = m.split("\n")
    a = re.match(RE_BUTTON, a)
    b = re.match(RE_BUTTON, b)
    p = re.match(RE_PRIZE, p)
    return Machine(
        a=XY(x=int(a[1]), y=int(a[2])),
        b=XY(x=int(b[1]), y=int(b[2])),
        prize=XY(x=int(p[1]) + 10000000000000, y=int(p[2]) + 10000000000000),
    )


def solve(machine) -> int:
    """Holy mathmatics Batman!

    Read the doc linked above to see what's going on in detail, but the general
    idea is that the machine presents a set of simultaneous equations that can
    be solved using matix multiplication.

    If we take the first machine from the input:

    Button A: X+15, Y+61
    Button B: X+66, Y+12
    Prize: X=1100, Y=4824

    This can be re-written as:

        15a + 66b = 1100
        61a + 12b = 4824

    Which we then solve using the system of matrix multiplication.
    """
    det = machine.a.x * machine.b.y - machine.a.y * machine.b.x

    a = machine.b.y * machine.prize.x - machine.b.x * machine.prize.y
    b = machine.a.x * machine.prize.y - machine.a.y * machine.prize.x

    if a % det != 0 or b % det != 0:
        return 0

    a = a / det
    b = b / det

    return int(3 * a + b)


def main():
    with open("q13/input.txt", "r") as fd:
        machines = fd.read().strip().split("\n\n")

    total = 0
    for m in machines:
        total += solve(parse(m))
    print(total)


if __name__ == "__main__":
    main()
