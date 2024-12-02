import sys
from part1 import read_input


def solve(l1: list, l2: list) -> int:
    similarity_score = 0

    l2_counts: dict[int, int] = {}
    for y in l2:
        if y in l2_counts:
            l2_counts[y] += 1
        else:
            l2_counts[y] = 1

    for x in l1:
        if x in l2_counts:
            similarity_score += x * l2_counts[x]

    return similarity_score


if __name__ == "__main__":
    l1, l2 = read_input(sys.argv[1])
    print(solve(l1, l2))
