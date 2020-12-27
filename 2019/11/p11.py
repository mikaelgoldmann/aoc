from lib19 import intcode as ic

import sys


def turn(dx, dy, to_right):
    return (dy, -dx) if to_right else (-dy, dx)


def main(start_white=False):
    with open(sys.argv[1]) as inp:
        prog = next(ic.read_prog(inp))
    grid = {}
    pos = 0, 0
    data = []
    idata = iter(data)
    run = ic.run(prog, idata, 0)
    running = True
    paint_step = True
    dx, dy = 0, 1
    nsteps = 0
    painted = set()
    if start_white:
        grid[pos] = 1
    data.append(grid.get(pos, 0))
    while running:
        mem, out, pc, running = next(run)
        nsteps += 1
        if out is not None:
            assert out in [0, 1]
            if paint_step:
                painted.add(pos)
                grid[pos] = out
                paint_step = False
            else:
                dx, dy = turn(dx, dy, to_right=out == 1)
                pos = pos[0] + dx, pos[1] + dy
                data.append(grid.get(pos, 0))
                paint_step = True
    return painted, grid
    print(len(painted))


def show_grid(g):
    minx, miny = next(iter(g.keys()))
    maxx, maxy = minx, miny
    for x, y in g.keys():
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    print (minx, miny, maxx, maxy)
    ncols = maxx - minx + 1
    nrows = maxy - miny + 1
    hull = [[' '] * ncols for i in range(nrows)]
    for (x,y), v in g.items():
        hull[y - miny][x - maxx] = '*' if v else ' '
    # because upside down...
    def prt(h):
        if not h:
            return
        prt(h[1:])
        print(''.join(h[0]))
    prt(hull)


if __name__ == '__main__':
    painted, grid = main()
    print("part 1", len(painted))
    painted, grid = main(start_white=True)
    print()
    print("part 2")
    show_grid(grid)