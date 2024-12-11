"""
Understanding
-------------
The input is a list of strings. Each "blink" means that each number in the list
changes according to some rules. The interesting rule is that if the number has
an even number of digits then it splits into two numbers by dividing the digits
in half.

Notes
-----
I tried simply keeping each stone to a string and taking each half using
slicing. But that was very slow when you got to about 8 blinks. (Although I
later came to regret this line of thinking, the slowness must have come from
somewhere else).

Rankings:

Day 11 - Time 05:30:17 - Rank 25745 - Score 0

Runs in 0.02s on my machine.
"""

from functools import cache
import math


@cache
def change_stone(stone):
    if stone == 0:
        yield 1
    else:
        digit_count = int(math.log10(stone)) + 1
        if digit_count % 2 == 0:
            exp = 10 ** (digit_count / 2)
            left_side = int(stone // exp)
            yield left_side
            right_side = int(stone - left_side * exp)
            yield right_side
        else:
            yield stone * 2024


def blink(stones):
    for stone in stones:
        yield from change_stone(stone)


def main():
    with open("q11/input.txt", "r") as fd:
        stones = list(map(int, fd.read().strip().split()))

    for _ in range(25):
        stones = blink(stones)

    stones = list(stones)
    # print(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
