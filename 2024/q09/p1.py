"""
Understanding
-------------

Rearrange individual file blocks on a harddrive to pack the blocks as close
together as possible (with as little free space between them).

Input is an alternatice sequence of file size and then free space.

e.g. 12345 means a file made up of one block, followed by 2 blocks of free space
followed by a file of 3 blocks, then 4 blocks free space, then a 5 block file.

Starting from the right hand side move blocks to the leftmost available free
space.

The answer is a "checksum" involving the file IDs (the file's original location)
and the block indecies that the file is located on.

Notes
-----

I was busy today, so I couldn't work on this until the evening after it was
published, resulting in a ranking of:

Day 9 - Time 18:06:52 - Rank 44934 - Score 0

I tried to make this one as efficient as I could, and I think it's pretty fast.
It takes 0.03s on my machine.

The general idea is to consume from both ends of the input at the same time,
moving blocks to the left. Stopping when you reach some kind of middle point.

When you're moving from left to right and you encounter a file, you can
calculate the checksum straightaway because you know you're not going to move a
file that you've processed from the left hand side.

When you're moving from right to left and you move some blocks around you can
calculate the checksum of the repositioned blocks because you know you won't
move them a second time.

There's a log of tracking of index positions, which feels a bit like code smell.
I'd normally try to avoid using the enumerate function as much as I have here.
"""


def main():
    with open("q09/input.txt", "r") as fd:
        input_ = list(map(int, fd.read().strip()))

    input_len = len(input_)
    checksum = 0

    forward = enumerate(input_)
    backward = enumerate(input_[::-1])

    # Ignore the first one, its checksum will always be 0
    fw_map_idx, fw_file_len = next(forward)
    fw_block_idx = fw_file_len
    # Second reading is the free space
    fw_map_idx, fw_free_len = next(forward)

    if input_len % 2 == 0:
        # If the disk map shows the amount of free space right at the end of the
        # disk, then read that value and discard it.
        next(backward)
    bw_map_idx, bw_file_len = next(backward)
    bw_block_idx = sum(i for i in input_) - 1

    while fw_map_idx < input_len - bw_map_idx - 1:
        if fw_free_len == 0:
            fw_map_idx, fw_file_len = next(forward)
            checksum += (fw_map_idx // 2) * sum(
                range(fw_block_idx, min(fw_block_idx + fw_file_len, bw_block_idx + 1))
            )
            fw_block_idx += fw_file_len
            fw_map_idx, fw_free_len = next(forward)
        elif bw_file_len == 0:
            # Skip over the free space
            bw_map_idx, bw_free_len = next(backward)
            bw_block_idx -= bw_free_len

            bw_map_idx, bw_file_len = next(backward)
        else:
            moved_blocks = min(fw_free_len, bw_file_len)

            checksum += ((input_len - bw_map_idx - 1) // 2) * sum(
                range(fw_block_idx, fw_block_idx + moved_blocks)
            )

            fw_block_idx += moved_blocks
            bw_block_idx -= moved_blocks
            fw_free_len -= moved_blocks
            bw_file_len -= moved_blocks

    print(checksum)


if __name__ == "__main__":
    main()
