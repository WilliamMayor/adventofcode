from collections import defaultdict


def is_correct(update, ordering_rules):
    for idx, page in enumerate(update):
        for next_page in update[idx + 1 :]:
            if next_page in ordering_rules[page]:
                return False
    return True


def main():
    with open("q5/input.txt", "r") as fd:
        input_ = fd.readlines()

    ordering_rules = [list(map(int, l.split("|"))) for l in input_ if "|" in l]
    updates = [
        list(map(int, l.split(","))) for l in input_ if "|" not in l and l.strip()
    ]

    rules = defaultdict(set)
    for first, second in ordering_rules:
        rules[second].add(first)

    total = 0
    for update in updates:
        if is_correct(update, rules):
            total += update[len(update) // 2]
    print(total)


if __name__ == "__main__":
    main()
