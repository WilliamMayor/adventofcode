from collections import defaultdict


def is_correct(update, ordering_rules):
    for idx, page in enumerate(update):
        for next_page in update[idx + 1 :]:
            if next_page in ordering_rules[page]:
                return False
    return True


def fix_update(update, ordering_rules):
    fixed = [update[0]]
    for page in update[1:]:
        for idx in range(len(fixed)):
            candidate = list(fixed)
            candidate.insert(idx, page)
            if is_correct(candidate, ordering_rules):
                fixed = candidate
                break
        else:
            fixed.append(page)
    return fixed


def main():
    with open("q05/input.txt", "r") as fd:
        input_ = fd.readlines()

    ordering_rules = [list(map(int, line.split("|"))) for line in input_ if "|" in line]
    updates = [
        list(map(int, line.split(",")))
        for line in input_
        if "|" not in line and line.strip()
    ]

    # This is a reverse lookup; given a page number tell me what has to go before it
    rules = defaultdict(set)
    for first, second in ordering_rules:
        rules[second].add(first)

    total = 0
    for update in updates:
        if not is_correct(update, rules):
            update = fix_update(update, rules)
            total += update[len(update) // 2]
    print(total)


if __name__ == "__main__":
    main()
