def main():
    with open("q9/input.txt", "r") as fd:
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
