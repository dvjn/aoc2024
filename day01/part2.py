import sys


def read_input(file_name: str) -> tuple[list, list]:
    l1, l2 = [], []
    with open(file_name) as input_file:
        for line in input_file:
            [x, y] = line.split("   ")
            l1.append(int(x))
            l2.append(int(y))
    return l1, l2


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
