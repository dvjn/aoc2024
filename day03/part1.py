import sys
from typing import Generator

def read_input(file_name: str) -> str:
    with open(file_name) as input_file:
        return input_file.read().replace("\n", "")

class CannotParse(Exception):
    pass

def parse_char(x: str, ch: str) -> str:
    if x[0] != ch:
        raise CannotParse()

    return x[1:]

def parse_number(x: str) -> tuple[str, int]:
    digits = ""
    while len(x) > 0 and x[0].isdigit():
        digits += x[0]
        x = x[1:]
    if digits == "":
        raise CannotParse()
    return x, int(digits)

def find_instructions(x: str) -> Generator[tuple[int, int], None, None]:
    while x:
        try:
            x = parse_char(x, "m")
            x = parse_char(x, "u")
            x = parse_char(x, "l")
            x = parse_char(x, "(")
            x, d1 = parse_number(x)
            x = parse_char(x, ",")
            x, d2 = parse_number(x)
            x = parse_char(x, ")")
            yield d1, d2
        except CannotParse:
            x = x[1:]

def solve(instructions: str) -> int:
    total = 0
    for x, y in find_instructions(instructions):
        total += x * y
    return total

if __name__ == "__main__":
    instructions = read_input(sys.argv[1])
    print(solve(instructions))
