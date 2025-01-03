import sys
from collections import defaultdict
from types import new_class


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


def get_int_lines(lines=None):
    if lines is None:
        lines = get_lines()
    int_lines = []
    for line in lines:
        int_line = []
        for x in line.split():
            try:
                x = int(x)
                int_line.append(x)
            except:
                pass
        int_lines.append(int_line)
    return int_lines


def bfs2(board, row, col):
    visited = defaultdict(lambda: 0)
    nrows = len(board)
    ncols = len(board[0])
    seen = {(row, col)}
    q = [(row, col)]
    hd = 0
    visited[(row, col)] = 1
    while hd < len(q):
        r,c = q[hd]
        hd += 1
        for r1, c1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if r1 < 0 or c1 < 0:
                continue
            if r1 >= nrows or c1 >= ncols:
                continue
            if board[r1][c1] == board[r][c] + 1:
                if not (r1, c1) in seen:
                    seen.add((r1, c1))
                    q.append((r1, c1))
                visited[(r1, c1)] += visited[(r, c)]
    return visited


def solve2(board):
    acc = 0
    nines = []
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == 9:
                nines.append((row, col))
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == 0:
                visited = bfs2(board, row, col)
                for (r, c) in nines:
                    if (r,c) in visited:
                        acc += visited[(r, c)]
    return acc


def solve1(board):
    acc = 0
    nines = []
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == 9:
                nines.append((row, col))
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == 0:
                visited = bfs2(board, row, col)
                for (r, c) in nines:
                    if visited[(r,c)] > 0: # in visited:
                        acc += 1
    return acc


def main(argv):
    board = [[int(c) for c in line] for line in get_lines()]
    print("part 1")
    print(solve1(board))
    print()
    print("part 2")
    print(solve2(board))


if __name__ == '__main__':
    main(sys.argv)
