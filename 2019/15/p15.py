import sys
from lib19 import intcode as ic

# Only four movement commands are understood: north (1), south (2), west (3), and east (4).
# Any other command is invalid. The movements differ in direction, but not in
# distance: in a long enough east-west hallway, a series of commands like
# 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

MOVE = {
    1: (0, 1),  # north
    2: (0, -1), # south
    3: (-1, 0), # west
    4: (1, 0)   # east
}


BACK = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


def run_to_inp(r):
    res = None
    while True:
        mem, out, pc, running = next(r)
        #print("pc", pc)
        if out is not None: res = out
        assert running
        xop = mem[pc]
        if ic.parse_op(xop)[0] == ic.OpCode.INP:
            return res


def dfs_go(floor, inp, r, d, pos):
    inp.append(d)
    out = run_to_inp(r)
    if out == 0:
        floor[pos] = '#'
    elif out == 1:
        floor[pos] = '.'
    elif out == 2:
        floor[pos] = 'X'
        print("Oxygene", pos)
    else:
        raise Exception("Illegal output", repr(out))
    # print(pos, floor[pos])
    if out == 0:
        return
    dfs(floor, pos, inp, r)
    # now, move back to where you were before
    inp.append(BACK[d])
    run_to_inp(r)


def dfs(floor, pos, inp, r):
    x, y = pos
    for d in [1, 2, 3, 4]:
        dx, dy = MOVE[d]
        pos1 = x + dx, y + dy
        if pos1 not in floor:
            # Try to go to pos1
            dfs_go(floor, inp, r, d, pos1)


def bfs(floor, start):
    dist = {start: 0}
    q = [start]
    hd = 0
    while hd < len(q):
        x, y = q[hd]
        hd += 1
        for d in [1, 2, 3, 4]:
            dx, dy = MOVE[d]
            pos = x + dx, y + dy
            if pos in dist or floor.get(pos, '#') == '#':
                continue
            dist[pos] = 1 + dist[(x,y)]
            q.append(pos)
    return dist


def print_floor(floor):
    print(floor)
    pos = list(floor.keys())
    xmin, ymin = pos[0]
    xmax, ymax = pos[0]
    for x, y in pos:
        xmin = min(x, xmin)
        ymin = min(y, ymin)
        xmax = max(x, xmax)
        ymax = max(x, ymax)
    print((xmin,ymin), (xmax, ymax))
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            sys.stdout.write(floor.get((x, y), ' '))
        print()


def solve1(prog):
    pos = 0, 0
    floor = {pos: '.'}
    inp = []
    r = ic.run(prog, iter(inp))
    run_to_inp(r)  # go to first input
    dfs(floor, pos, inp, r)
    print_floor(floor)
    dist = bfs(floor, (0,0))
    [oxygene] = [pos for pos in floor if floor[pos] == 'X']
    print("step 1", dist[oxygene])
    dist = bfs(floor, oxygene)
    print("step 2", max(dist.values()))


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    with open('15.in') as f:
        prog = next(ic.read_prog(f))
        solve1(prog)