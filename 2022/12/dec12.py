import sys
from collections import deque


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_grid(lines):
    S = (-1, -1)
    E = (-1, -1)
    ncol = len(lines[0])
    nrow = len(lines)
    grid = [[1000]*(ncol + 2) for i in range(nrow + 2)]
    for r, line in enumerate(lines):
        for c, x in enumerate(line):
            if x == 'S':
                S = (r+1, c+1)
                grid[r+1][c+1] = ord('a')
            elif x == 'E':
                E = (r+1, c+1)
                grid[r+1][c+1] = ord('z')
            else:
                grid[r+1][c+1] = ord(x)
    return grid, S, E


def visit(r, c, seen, grid, r1, c1, q, n):
    val = grid[r1][c1]
    if (r, c) in seen:

        return
    if grid[r][c] > val + 1:
        return
    seen[(r, c)] = (r1, c1)
    q.append(((r,c), n))


def visit_down(r, c, seen, grid, r1, c1, q, n):
    val = grid[r1][c1]
    print(r, c, r1, c1)
    if grid[r][c] > 500:
        return
    if (r, c) in seen:
        return
    if grid[r][c] < val - 1:
        return
    seen[(r, c)] = (r1, c1)
    q.append(((r,c), n))


def bfs(grid, pos, goal):
    q = deque()
    q.append((pos, 0))
    seen = {pos: None}
    while True:
        (r, c), n = q.popleft()
        #print(((r,c),n))
        if (r, c) == goal:
            return n
        visit(r + 1, c, seen, grid, r, c, q, n + 1)
        visit(r - 1, c, seen, grid, r, c, q, n + 1)
        visit(r, c + 1, seen, grid, r, c,  q, n + 1)
        visit(r, c - 1, seen, grid, r, c,  q, n + 1)
        # print(q)
        #print(seen)


def bfs_down(grid, pos):
    q = deque()
    q.append((pos, 0))
    seen = {pos: None}
    while True:
        (r, c), n = q.popleft()
        #print(((r,c),n))
        val = grid[r][c]
        if  val == ord('a'):
            return n
        visit_down(r + 1, c, seen, grid, r, c, q, n + 1)
        visit_down(r - 1, c, seen, grid, r, c, q, n + 1)
        visit_down(r, c + 1, seen, grid, r, c,  q, n + 1)
        visit_down(r, c - 1, seen, grid, r, c,  q, n + 1)
        # print(q)
        #print(seen)


if __name__ == '__main__':
    lines = get_lines()
    grid, S, E = get_grid(lines)
    for row in grid:
        print(row)
    print()
    print("part 1")
    print(bfs(grid, S, E))


    print()
    print("part 2")
    print(bfs_down(grid, E))
