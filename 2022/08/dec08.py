import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_trees(f=None):
    lines = get_lines(f)
    return [get_tree_row(line) for line in lines]


def get_tree_row(row):
    return [int(x) for x in row]


def seen_trees(trees, row, col, drow, dcol, seen):
    h = -1
    while row >= 0 and row < len(trees) and col >= 0 and col < len(trees[0]):
        if trees[row][col] > h:
            seen.add((row, col))
            h = trees[row][col]
        row += drow
        col += dcol

def find_seen_trees(trees):
    seen = set()
    nrows = len(trees)
    ncols = len(trees[0])
    for row in range(nrows):
        seen_trees(trees, row, 0, 0, 1, seen)
        seen_trees(trees, row, ncols - 1, 0, -1, seen)
    for col in range(ncols):
        seen_trees(trees, 0, col, 1, 0, seen)
        seen_trees(trees, nrows - 1, col, -1, 0, seen)
    return seen


def select(r, c, dr, dc):
   return r if dr != 0 else c


def comp1(trees, row, col, drow, dcol, cnt, pos):
    row += drow
    col += dcol
    while row >= 0 and row < len(trees) and col >= 0 and col < len(trees[0]):
        h = trees[row][col]
        p = select(row, col, drow, dcol)
        if drow + dcol == 1:
            f = max
        else:
            f = min
        v = pos[h]
        for h1 in range(h, 10):
            v = f([v, pos[h1]])
        pos[h] = p
        cnt[row][col] = abs(v - p)
        row += drow
        col += dcol


def comp(trees):
    nrows = len(trees)
    ncols = len(trees[0])
    up = [[0 for c in range(ncols)] for r in range(nrows)]
    down = [[0 for c in range(ncols)] for r in range(nrows)]
    left = [[0 for c in range(ncols)] for r in range(nrows)]
    right = [[0 for c in range(ncols)] for r in range(nrows)]
    for row in range(nrows):
        comp1(trees, row, 0, 0, 1, left, [0] * 10)
        comp1(trees, row, ncols - 1, 0, -1, right, [ncols - 1] * 10)
    for col in range(ncols):
        comp1(trees, 0, col, 1, 0, up, [0] * 10)
        comp1(trees, nrows - 1, col, -1, 0, down, [nrows - 1] * 10)
    mx = 0
    for row in range(1, nrows - 1):
        for col in range(1, ncols - 1):
            p = up[row][col] * down[row][col] * left[row][col] * right[row][col]
            if p > mx:
                mx = p
    return mx


if __name__ == '__main__':
    trees = get_trees()

    print("part 1")
    print(len(find_seen_trees(trees)))

    print()
    print("part 2")
    print(comp(trees))
