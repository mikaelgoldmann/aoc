import sys
import re
import copy

TILE = re.compile('Tile ([0-9]+):')
ROW = re.compile('([.#]+)')

SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]


def get_monster():
    return [
        [c for c in line] for line in SEA_MONSTER
    ]


def sqrt(n):
    for i in range(n):
        if i * i > n:
            raise Exception("not a square")
        elif i * i == n:
            return i
    raise Exception("no solution")


def sides(tile):
    return (
        as_num(tile[0]),
        as_num((r[-1] for r in tile)),
        as_num(tile[-1]),
        as_num((r[0] for r in tile))
    )


class Orientation(object):
    def __init__(self, tile):
        self.tile = tile
        self.top = top(tile)
        self.bottom = bottom(tile)
        self.left = left(tile)
        self.right = right(tile)


def orientations(rows):
    options = []
    for flipped in [False, True]:
        for times in range(4):
            r1 = rot_left(rows, times)
            if flipped:
                r1 = flip_top_bottom(r1)
            options.append(Orientation(r1))
    return options


def read_tile(inp):
    m = TILE.match(inp.readline())
    assert m
    tile = int(m.group(1))
    rows = []
    for i in range(10):
        m = ROW.match(inp.readline())
        assert m
        rows.append([x for x in m.group(1)])
    return tile, orientations(rows)


def read_tiles(inp):
    tiles = [read_tile(inp)]
    while inp.readline():
        tiles.append(read_tile(inp))
    return tiles


def flip_top_bottom(tile):
    t = []
    for row in tile:
        t = [row[:]] + t
    return t


def rot_left(tile, times=1):
    assert times >= 0
    if times == 0:
        return copy.deepcopy(tile)

    t = [[] for _ in tile[0]]
    for i, row in enumerate(tile):
        for j, c in enumerate(row):
            k = len(row) - 1 - j
            assert len(t[k]) == i
            t[k].append(c)
    return rot_left(t, times - 1)


def as_num(s):
    n = 0
    for c in s:
        n *= 2
        if c == '#':
            n += 1
    return n


def rev_num(n):
    m = 0
    for i in range(10):
        m *= 10
        m += n % 10
        n //= 10
    return m


def flip(nums):
    assert len(nums) == 4
    tp, lft, bot, rgt = nums
    return rev_num(tp), rev_num(rgt), rev_num(bot), rev_num(lft)


def enum(n):
    for s in range(2 * n - 1):
        for x in range(n):
            y = s - x
            if 0 <= y < n:
                yield x, y


def top(r): return as_num(r[0])


def bottom(r): return as_num(r[-1])


def left(r): return as_num([r1[0] for r1 in r])


def right(r): return as_num([r1[-1] for r1 in r])


def fits(piece, grid, r, c):
    if r > 0:
        if grid[r - 1][c][1].bottom != piece.top:
            return False
    if c > 0:
        if grid[r][c - 1][1].right != piece.left:
            return False
    return True


def solve(grid, used, tiles, pos, num):
    if num == len(pos):
        return grid
    r, c = pos[num]
    for i, orientations in tiles:
        if i in used:
            continue
        for orientation in orientations:
            if fits(orientation, grid, r, c):
                used.add(i)
                grid[r][c] = (i, orientation)
                sol = solve(grid, used, tiles, pos, num + 1)
                if sol is not None:
                    return sol
                else:
                    used.remove(i)
    return None


def trim_tile(tile):
    tile1 = []
    for row in tile[1:-1]:
        tile1.append(row[1:-1])
    return tile1


def flatten(grid):
    tile0x0 = grid[0][0]
    nrows = len(tile0x0)
    flat = []
    for tile_row in grid:
        for i in range(nrows):
            row = []
            for tile in tile_row:
                row.extend(tile[i])
            flat.append(row)
    return flat


def get_image(grid, N):
    grid1 = [[[]] * N for i in range(N)]
    for r in range(N):
        for c in range(N):
            grid1[r][c] = trim_tile(grid[r][c][1].tile)
    return flatten(grid1)


def print_image(image):
    for row in image:
        print(''.join(row))


def print_grid(grid):
    g = []
    for row in grid:
        r = []
        for i, t in row:
            r.append(t)
        g.append(r)
    print_image(flatten(g))


def match(image, pattern, r0, c0):
    pnr = len(pattern)
    pnc = len(pattern[0])
    inr = len(image)
    inc = len(image[0])
    if r0 + pnr > inr:
        return False
    if c0 + pnc > inc:
        return False
    for r1 in range(pnr):
        for c1 in range(pnc):
            if pattern[r1][c1] == '#' and image[r0 + r1][c0 + c1] != '#':
                return False
    return True


def count_pattern(image, pattern):
    # foo =''.join(image[0])
    # if foo != '.####...#####..#...###..':
    #     return False

    # print("---------")
    # print_image(pattern)
    # print()
    # print_image(image)
    pnr = len(pattern)
    pnc = len(pattern[0])
    inr = len(image)
    inc = len(image[0])
    nmatches = 0
    for r0 in range(inr - pnr + 1):
        for c0 in range(inc - pnc + 1):
            if match(image, pattern, r0, c0):
                nmatches += 1
    return nmatches


def main():
    with open(sys.argv[1]) as f:
        tiles = read_tiles(f)
    print("tile count", len(tiles))
    used = set()
    N = sqrt(len(tiles))
    grid = [[[]] * N for i in range(N)]
    grid = solve(grid, used, tiles, list(enum(N)), 0)
    # print("YES" if grid else "NO")

    # print_image(flatten(grid))
    for row in grid:
        ids = []
        for i, x in row:
            ids.append(i)
        #print(ids)
    prod = 1
    for x in [0, -1]:
        for y in [0, -1]:
            prod *= grid[x][y][0]
    print("part 1", prod)
    #print_grid(grid)

    #print()
    #print_image(get_image(grid, N))

    monster = get_monster()
    images = orientations(get_image(grid, N))
    monster_count = 0
    for image in images:
        num = count_pattern(image.tile, monster)
        if num:
            print("monster count", num)
            monster_count = num
    cnt1 = count_pattern(images[0].tile, [['#']])
    cnt2 = count_pattern(monster, [['#']])
    print(cnt1, cnt2)
    # We are now assuming that no '#' is part of more than one monster
    # Or in other words that no monster matchings overlap
    print("part 2", cnt1 - cnt2 * monster_count)



if __name__ == '__main__':
    main()
