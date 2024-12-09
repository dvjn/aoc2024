import sys


def read_input(file_name: str) -> list[list[int]]:
    reports = []
    with open(file_name) as input_file:
        for line in input_file:
            report = [int(x) for x in line.split()]
            reports.append(report)
    return reports


def get_sign(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def is_safe(report: list[int]) -> bool:
    dampening = 1
    direction = get_sign(report[1] - report[0])
    previous = report[0]
    for current in report[1:]:
        if not (0 < direction * (current - previous) < 4):
            if dampening > 0:
                dampening -= 1
                continue
            return False
        previous = current
    return True


def solve(reports: list[list[int]]) -> int:
    return sum(1 for report in reports if is_safe(report) or is_safe(report[::-1]))


if __name__ == "__main__":
    reports = read_input(sys.argv[1])
    print(solve(reports))
