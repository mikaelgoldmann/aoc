import sys


def parse(x):
    return [ int(c == '#') for c in x.strip()]


lines = [parse(x.strip()) for x in sys.stdin]

nr = len(lines)
nc = len(lines[0])


def empty_layer(nr, nc):
    return [ [0 for i in range(nc)] for j in range(nr) ]

def empty_grid3(nr, nc, h):
    return [ empty_layer(nr, nc) for k in range(h) ]

def empty_grid4(nr, nc, nz, nw):
    return [ empty_grid3(nr, nc, nz) for w in range(nw)]

padding = 7

grid = empty_grid4(nr + 2 * padding, nc + 2 * padding, 1 + 2 * padding, 1 + 2 * padding)

for r in range(nr):
    for c in range(nc):
        grid[padding][padding][r + padding][c + padding] = lines[r][c]


def count3x3x3x3(g, r, c, z, w):
    s = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    s += g[w+dw][z+dz][r+dr][c+dc]
    return s - g[w][z][r][c]


def step(g, nr, nc, nz, nw):
    g1 = empty_grid4(nr, nc, nz, nw)
    for r in range(1, nr - 1): 
        for c in range(1, nc - 1): 
            for z in range(1, nz - 1):
                for w in range(1, nw - 1):
                    state = g[w][z][r][c]
                    cnt = count3x3x3x3(g, r, c, z, w)
                    if state:
                        g1[w][z][r][c] = (cnt in [2, 3])
                    else:
                        g1[w][z][r][c] = (cnt  == 3)
    return g1


def show(grid):
    for cube in grid:
        for layer in cube:
            for row in layer:
                for x in row:
                    sys.stdout.write('#' if x else '.')
                print()
            print()
        print()

#show(grid)

for i in range(6):
    grid = step(grid, nr + 2 * padding, nc + 2 * padding, 1 + 2 * padding, 1 + 2 * padding)
    # show(grid)

s = 0
for cube in grid:
    for layer in cube:
        for row in layer:
            s += sum(row)





print("part 2", s)
