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

    print("Hoping for less than 6848626407700")


if __name__ == "__main__":
    main()
