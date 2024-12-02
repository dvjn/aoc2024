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
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)

    distance = 0
    for x, y in zip(sorted_l1, sorted_l2):
        distance += abs(x - y)

    return distance


if __name__ == "__main__":
    l1, l2 = read_input(sys.argv[1])
    print(solve(l1, l2))
