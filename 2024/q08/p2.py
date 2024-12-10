import itertools
from collections import defaultdict


def parse_input(input_):
    antenna = defaultdict(set)
    for row_idx, row in enumerate(input_):
        for col_idx, cell in enumerate(row):
            if cell != ".":
                antenna[cell].add((row_idx, col_idx))
    return antenna


def find_antinodes(input_, node_a, node_b):
    distance = (node_a[0] - node_b[0], node_a[1] - node_b[1])
    yield node_a
    yield node_b
    next_node = (node_a[0] + distance[0], node_a[1] + distance[1])
    while is_in_bounds(next_node, input_):
        yield next_node
        next_node = (next_node[0] + distance[0], next_node[1] + distance[1])
    next_node = (node_b[0] - distance[0], node_b[1] - distance[1])
    while is_in_bounds(next_node, input_):
        yield next_node
        next_node = (next_node[0] - distance[0], next_node[1] - distance[1])


def is_in_bounds(node, input_):
    if node[0] < 0 or node[1] < 0:
        return False
    try:
        input_[node[0]][node[1]]
        return True
    except IndexError:
        return False


def print_map(input_, a, b, antinodes):
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    OKGREEN = "\033[92m"
    for row_idx, row in enumerate(input_):
        for col_idx, cell in enumerate(row):
            if (row_idx, col_idx) in antinodes:
                if cell == ".":
                    cell = "#"
                print(f"{FAIL}{cell}{ENDC}", end="")
            elif (row_idx, col_idx) in (a, b):
                print(f"{OKGREEN}{cell}{ENDC}", end="")
            else:
                print(cell, end="")


def main():
    with open("q08/input.txt", "r") as fd:
        input_ = fd.read().strip().split()

    antinodes = set()
    antenna = parse_input(input_)
    for letter, positions in antenna.items():
        for node_a, node_b in itertools.combinations(positions, 2):
            for antinode in find_antinodes(input_, node_a, node_b):
                antinodes.add(antinode)
    print(len(antinodes))


if __name__ == "__main__":
    main()
