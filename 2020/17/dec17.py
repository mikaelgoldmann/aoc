import sys


def parse(x):
    return [ int(c == '#') for c in x.strip()]


lines = [parse(x.strip()) for x in sys.stdin]

nr = len(lines)
nc = len(lines[0])


def empty_layer(nr, nc):
    return [ [0 for i in range(nc)] for j in range(nr) ]

def empty_grid(nr, nc, h):
    return [ empty_layer(nr, nc) for k in range(h) ]


padding = 7

grid = empty_grid(nr + 2 * padding, nc + 2 * padding, 1 + 2 * padding)

for r in range(nr):
    for c in range(nc):
        grid[padding][r + padding][c + padding] = lines[r][c]


def count3x3x3(g, r, c, z):
    s = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            for dz in range(-1, 2):
                s += g[z+dz][r+dr][c+dc]
    return s - g[z][r][c]


def step(g, nr, nc, h):
    g1 = empty_grid(nr, nc, h)
    for r in range(1, nr - 1): 
        for c in range(1, nc - 1): 
            for z in range(1, h - 1):
                state = g[z][r][c]
                cnt = count3x3x3(g, r, c, z)
                if state:
                    g1[z][r][c] = (cnt in [2, 3])
                else:
                    g1[z][r][c] = (cnt  == 3)
    return g1


def show(grid):
    for layer in grid:
        for row in layer:
            for x in row:
                sys.stdout.write('#' if x else '.')
            print()
        print()

#show(grid)

for i in range(6):
    grid = step(grid, nr + 2 * padding, nc + 2 * padding, 1 + 2 * padding)
    # show(grid)

s = 0
for layer in grid:
    for row in layer:
        s += sum(row)




print("part 1", s)


print("part 2", None)
