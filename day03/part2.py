import sys
from dataclasses import dataclass
from typing import Generator, Protocol

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

@dataclass
class State:
    enabled: bool = True
    result: int = 0

class Instruction(Protocol):
    @classmethod
    def parse(cls, x: str) -> tuple[str, "Instruction"]: ...
    def run(self, state: State) -> State: ...

@dataclass
class Mul:
    x: int
    y: int

    @classmethod
    def parse(cls, x: str) -> tuple[str, "Mul"]:
        x = parse_char(x, "m")
        x = parse_char(x, "u")
        x = parse_char(x, "l")
        x = parse_char(x, "(")
        x, d1 = parse_number(x)
        x = parse_char(x, ",")
        x, d2 = parse_number(x)
        x = parse_char(x, ")")
        return x, cls(d1, d2)

    def run(self, state: State) -> State:
        if state.enabled:
            state.result += self.x * self.y
        return state

@dataclass
class Do:
    @classmethod
    def parse(cls, x: str) -> tuple[str, "Do"]:
        x = parse_char(x, "d")
        x = parse_char(x, "o")
        x = parse_char(x, "(")
        x = parse_char(x, ")")
        return x, cls()

    def run(self, state: State) -> State:
        state.enabled = True
        return state

@dataclass
class Dont:
    @classmethod
    def parse(cls, x: str) -> tuple[str, "Dont"]:
        x = parse_char(x, "d")
        x = parse_char(x, "o")
        x = parse_char(x, "n")
        x = parse_char(x, "'")
        x = parse_char(x, "t")
        x = parse_char(x, "(")
        x = parse_char(x, ")")
        return x, cls()

    def run(self, state: State) -> State:
        state.enabled = False
        return state

def find_instructions(x) -> Generator[Instruction, None, None]:
    while x:
        for instruction in (Mul, Dont, Do):
            try:
                x, instruction = instruction.parse(x)
                yield instruction
                break
            except CannotParse:
                pass
        else:
            x = x[1:]

def solve(instructions: str) -> int:
    state = State()
    for instruction in find_instructions(instructions):
        state = instruction.run(state)
    return state.result

if __name__ == "__main__":
    instructions = read_input(sys.argv[1])
    print(solve(instructions))
