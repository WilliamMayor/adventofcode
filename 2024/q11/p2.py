"""
Understanding
-------------

Same problem as part one, but now you have to run it 75 times, not 25.

Notes
-----

Really struggled with this one. My part one solution takes up too much memory
and uses 100% CPU as soon as you get to about 35 generations.

I re-wrote it a few times; using recursion to avoid having to keep large lists,
using bitmasks to try to speed up the modulo and divmod operations, heavy
caching to avoid repeating blinking the same stone multiple times. Nothing
worked, although I did get some good speed ups compared to my previous solution.

I ended up looking on the sub-reddit for some hints. I was surprised that people
were using string manipulation as that had been slow for me in part one, I think
that means that my profiling in part one hadn't revealed the true cause of my
slower code, it wasn't the string manipulations. Either that, or when you get to
higher generations (bigger lists) string manipulations stop being the limiting
factor.

Anyway:

Day 11 - Time 14:02:06 - Rank 30416 - Score 0

Runs in 0.07s on my machine.

"""

from collections import defaultdict


def blink(counts: dict[str, int]) -> dict[str, int]:
    next_counts = defaultdict(int)
    for stone, count in counts.items():
        if stone == "0":
            next_counts["1"] += count
        elif len(stone) % 2 == 0:
            middle = len(stone) // 2
            next_counts[stone[:middle]] += count
            next_counts[str(int(stone[middle:]))] += count
        else:
            next_counts[str(int(stone) * 2024)] += count
    return next_counts


def main():
    with open("q11/input.txt", "r") as fd:
        stones: list[str] = fd.read().strip().split()

    counts: dict[str, int] = defaultdict(int)

    for stone in stones:
        counts[stone] += 1

    for _ in range(75):
        counts = blink(counts)

    print(sum(counts.values()))


if __name__ == "__main__":
    main()
