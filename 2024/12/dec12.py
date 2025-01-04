from collections import deque
import sys


BORDER = '.'


DEBUG = False


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def mk_board(lines):
    ncols = len(lines[0])
    border = [BORDER for i in range(ncols + 2)]
    board = [border[:]]
    for line in lines:
        row = [BORDER]
        row.extend([c for c in line])
        row.append(BORDER)
        board.append(row)
    board.append(border[:])
    return board


def left(rc):
    r, c = rc
    return r, c - 1


def right(rc):
    r, c = rc
    return r, c + 1


def up(rc):
    r, c = rc
    return r - 1, c


def down(rc):
    r, c = rc
    return r + 1, c


def get_color(board, rc): return board[rc[0]][rc[1]]


def explore(board, rc):
    color =  get_color(board, rc)
    if color == BORDER:
        return 0, 0, set()
    q = deque()
    q.append(rc)
    area = 1
    circumference = 0
    seen = {rc}
    while q:
        rc = q.popleft()
        for f in [left, up, right, down]:
            rc1 = f(rc)
            if rc1 in seen:
                continue
            color1 =  get_color(board, rc1)
            if color1 == color:
                area += 1
                q.append(rc1)
                seen.add(rc1)
            else:
                circumference += 1
    dprint(rc, color, area, circumference, seen)
    return area, circumference, seen


def explore2(board, rc):
    color =  get_color(board, rc)
    if color == BORDER:
        return 0, 0, set()
    q = deque()
    q.append(rc)
    area = 1
    circumference = 0
    seen = {rc}
    while q:
        rc = q.popleft()
        for f in [left, up, right, down]:
            rc1 = f(rc)
            if rc1 in seen:
                continue
            color1 =  get_color(board, rc1)
            if color1 == color:
                area += 1
                q.append(rc1)
                seen.add(rc1)
        # edge below rc ends if it's turns up or down to the right
        downc = get_color(board, down(rc))
        if downc != color:
            if get_color(board, right(rc)) != color:
                circumference += 1
            elif get_color(board, down(right(rc))) == color:
                circumference += 1
        # edge above rc ends if it's turns up or down to the right
        upc = get_color(board, up(rc))
        if upc != color:
            if get_color(board, right(rc)) != color:
                circumference += 1
            elif get_color(board, up(right(rc))) == color:
                circumference += 1
        # edge left of rc ends if it's turns left or right below
        leftc = get_color(board, left(rc))
        if leftc != color:
            if get_color(board, down(rc)) != color:
                circumference += 1
            elif get_color(board, left(down(rc))) == color:
                circumference += 1
        # edge right of rc ends if it's turns left or right below
        rightc = get_color(board, right(rc))
        if rightc != color:
            if get_color(board, down(rc)) != color:
                circumference += 1
            elif get_color(board, right(down(rc))) == color:
                circumference += 1

    dprint(rc, color, area, circumference, seen)
    return area, circumference, seen


def solve(board, exploreation):
    nrows = len(board)
    ncols = len(board[0])
    acc = 0
    visited = set()
    for r in range(nrows):
        for c in range(ncols):
            if (r, c) not in visited:
                area, circumference, seen = exploreation(board, (r, c))
                acc += area * circumference
                visited.update(seen)
    return acc


def main(argv):
    lines = get_lines()
    print("part 1")
    board = mk_board(lines)
    print(solve(board, explore))
    print()
    print("part 2")
    print(solve(board, explore2))


if __name__ == '__main__':
    main(sys.argv)
