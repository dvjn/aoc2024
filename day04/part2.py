import sys

def read_input(filename: str) -> list[list[str]]:
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def solve(instructions: list[list[str]]) -> int:
    sum = 0
    for i in range(1, len(instructions) - 1):
        for j in range(1, len(instructions[i]) - 1):
            if instructions[i][j] == "A":
                try:
                    forward_diagonal = {instructions[i +1][j + 1], instructions[i - 1][j - 1]}
                    backward_diagonal = {instructions[i - 1][j + 1], instructions[i + 1][j - 1]}
                except IndexError:
                    continue
                else:
                    if forward_diagonal == backward_diagonal == {"M", "S"}:
                        sum += 1


    return sum

if __name__ == "__main__":
    instructions = read_input(sys.argv[1])
    print(solve(instructions))
