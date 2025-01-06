import sys
import argparse
from copy import deepcopy

DEBUG = False


LEFT, RIGHT, UP, DOWN = list(iter("<>^v"))


D = {
    LEFT: (0, -1),
    RIGHT: (0, 1),
    UP: (-1, 0),
    DOWN: (1, 0)
}


ROBOT = '@'
SPACE = '.'
BOX = 'O'
BORDER = '#'


def dprint(*a, **kw):
    if DEBUG:
        print(*a, **kw)


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_paragraphs(lines=None):
    if lines is None:
        lines = get_lines()
    paragraph = []
    for x in lines:
        x = x.strip()
        if not x:
            yield paragraph
            paragraph = []
        else:
            paragraph.append(x)
    if paragraph:
        yield paragraph


def parse_board(lines):
    return [list(iter(line)) for line in lines]


def parse_moves(lines):
    return ''.join(lines)


def step(board, r, c, move):
    dr, dc = D[move]
    r1, c1 = r + dr, c + dc
    while board[r1][c1] == BOX:
        r1, c1 = r1 + dr, c1 + dc
    if board[r1][c1] == BORDER:
        # cannot move
        return r, c
    r2, c2 = r + dr, c + dc
    board[r1][c1] = board[r2][c2]
    board[r][c] = SPACE
    board[r2][c2] = ROBOT
    return r2, c2


def find_cells(board, value):
    cells = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == value:
                cells.append((r, c))
    return cells


def solve1(board, moves):
    robots = find_cells(board, ROBOT)
    assert len(robots) == 1
    r, c = robots[0]
    for m in moves:
        r, c = step(board, r, c, m)
    boxes = find_cells(board, BOX)
    return sum( r * 100 + c for r, c in boxes)


def main(inp):
    paragraphs = [p for p in get_paragraphs(inp)]
    board = parse_board(paragraphs[0])
    moves = parse_moves(paragraphs[1])
    print("part 1")
    print(solve1(deepcopy(board), deepcopy(moves)))
    print()
    print("part 2")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", type=bool, default=False)
    parser.add_argument("--file", type=str)
    args = parser.parse_args(sys.argv[1:])
    DEBUG = args.debug
    with open(args.file) as inp:
        main(inp)
