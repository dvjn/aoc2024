import sys

def read_input(filename: str) -> list[list[str]]:
    with open(filename) as f:
        return [list(line.strip()) for line in f]

directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

def find_word_at(instructions: list[list[str]], direction: tuple[int, int], x: int, y: int, word: str) -> bool:
    if word == "":
        return True

    if x < 0 or y < 0:
        return False

    try:
        current = instructions[x][y]
    except IndexError:
        return False

    if current == word[0]:
        return find_word_at(instructions, direction, x + direction[0], y + direction[1], word[1:])

    return False

def solve(instructions: list[list[str]]) -> int:
    sum = 0
    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            for direction in directions:
                if find_word_at(instructions, direction, i, j, "XMAS"):
                    sum+=1
    return sum

if __name__ == "__main__":
    instructions = read_input(sys.argv[1])
    print(solve(instructions))
