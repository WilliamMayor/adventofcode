"""
Understanding
-------------

Building on Part 1, instead of moving individual blocks around, you now have to
move whole files from the right to the left, if they'll fit.

You only try to move the file once, even if subsequent file relocations have
opened up enough free space to move the file in a second pass.

Notes
-----

Part 2 took me about 1h20m after part 1:

Day 9 - Time 19:44:24 - Rank 35206 - Score 0

This one doesn't feel as efficient as Part 1, lots more loops. But it still runs
in 1.05s on my machine, so I'm happy.

The approach I took was to do a first pass over the input finding all the free
space slots (and their sizes). Then move backwards through the input adding
files to those free slots where they would fit. When you move a file, calculate
its checksum.

Finally, do a third pass in order to calculate the checksum for any files that
didn't get moved around.

I quickly spotted that moving a small file into a large free space would still
leave free space available. So you have to track the remaining space and the
remaining free locations.

The part I missed, the part I probably spent most of the hour trying to fix, was
that when you loop through the free space from left to right, you should stop
when the free space is to the right of the file you're considering. Obvious now
I know the answer, but that's what I missed this time around.
"""


def main():
    with open("q9/input.txt", "r") as fd:
        input_ = list(map(int, fd.read().strip()))

    input_len = len(input_)
    checksum = 0

    free_space = []
    block_indicies = {}
    block_idx = 0
    for map_idx, block_len in enumerate(input_):
        block_indicies[map_idx] = block_idx
        if map_idx % 2 != 0:
            free_space.append((map_idx, block_idx, block_len))
        block_idx += block_len

    moved_files = set()
    for bw_map_idx, file_len in enumerate(input_[::-1]):
        if bw_map_idx % 2 != 0:
            # Skip the free space indicators
            continue
        fw_map_idx = input_len - bw_map_idx - 1
        for fs_idx, (map_idx, block_idx, free_len) in enumerate(free_space):
            if map_idx > fw_map_idx:
                break
            if free_len >= file_len:
                free_space[fs_idx] = (
                    map_idx,
                    block_idx + file_len,
                    free_len - file_len,
                )
                moved_files.add(fw_map_idx)
                checksum += (fw_map_idx // 2) * sum(
                    range(block_idx, block_idx + file_len)
                )
                break

    for map_idx, file_len in enumerate(input_):
        if map_idx % 2 != 0:
            continue
        if map_idx not in moved_files:
            b_idx = block_indicies[map_idx]
            checksum += (map_idx // 2) * sum(range(b_idx, b_idx + file_len))

    print(checksum)


if __name__ == "__main__":
    main()
