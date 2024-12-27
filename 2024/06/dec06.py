import sys
from selectors import SelectSelector


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


def get_start(board):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if board[r][c] == '^':
                return r, c
    raise Exception('Start not found')


def do_step(pos, delta):
    x, y = pos
    dx, dy = delta
    return x + dx, y + dy


TURN = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}


OUTSIDE = ' '


def get_cell(board, pos):
    r, c = pos
    if r < 0 or c < 0:
        return OUTSIDE
    if r >= len(board) or c >= len(board[0]):
        return OUTSIDE
    return board[r][c]


def do_walk1(board, pos):
    visited = [[0] * len (board[0]) for i in range(len(board))]
    delta = -1, 0
    while True:
        visited[pos[0]][pos[1]] = 1
        next_pos = do_step(pos, delta)
        content = get_cell(board, next_pos)
        if content == OUTSIDE:
            return visited
        elif content == '#':
            # print("next_pos =", next_pos)
            delta =TURN[delta]
        else:
            pos = next_pos


def do_walk2(board, pos):
    visited = [[set() for j in range(len (board[0]))] for i in range(len(board))]
    delta = -1, 0
    while True:
        visited[pos[0]][pos[1]].add(delta)
        next_pos = do_step(pos, delta)
        content = get_cell(board, next_pos)
        if content == OUTSIDE:
            return False
        elif content == '#':
            # print("next_pos =", next_pos)
            delta =TURN[delta]
        elif delta in visited[next_pos[0]][next_pos[1]]:
            return True
        else:
            pos = next_pos


def solve1(board):
    start = get_start(board)
    visited = do_walk1(board, start)
    return sum(map(sum, visited))


def solve2(board):
    start = get_start(board)
    visited = do_walk1(board, start)
    tot = 0
    board1 = [ [ch for ch in row] for row in board]
    for r in range(len(visited)):
        for c in range(len(visited[0])):
            if not visited[r][c] or (r, c) == start:
                continue
            tmp = board1[r][c]
            board1[r][c] = '#'
            if do_walk2(board1, start):
                tot += 1
            board1[r][c] = tmp
    return tot


def main(argv):
    board = get_lines()
    print("part 1")
    print(solve1(board))
    print()
    print("part 2")
    print(solve2(board))


if __name__ == '__main__':
    main(sys.argv)
