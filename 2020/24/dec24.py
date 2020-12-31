import sys
from collections import defaultdict


"""
  origin  0,  0
  e       1,  0
  w      -1,  0
  ne      0,  1
  sw      0, -1  
  se      1, -1
  nw     -1,  1
"""

DELTA = {
    'e':  (1, 0),
    'w':  (-1, 0),
    'ne': (0, 1),
    'sw': (0, -1),
    'se': (1, -1),
    'nw': (-1, 1)
}


def parse_steps(line):
    line = line.strip()
    i = 0
    steps = []
    while i < len(line):
        if line[i] in DELTA:
            steps.append(DELTA[line[i]])
            i += 1
        elif line[i:i+2] in DELTA:
            steps.append(DELTA[line[i:i+2]])
            i += 2
        else:
            raise Exception("parse failure at", line[i:])
    return steps


def read_input(inp):
    return [parse_steps(line) for line in inp]


def move(pt, d):
    x, y = pt
    dx, dy = d
    return x + dx, y + dy


def make_floor(steps_list):
    floor = defaultdict(lambda: 1)
    for steps in steps_list:
        pos = 0, 0
        for step in steps:
            pos = move(pos, step)
        col = floor[pos]
        floor[pos] = 1 - col
    return floor


def solve1(floor):
    return count_black_tiles(floor)


def flip(floor):
    count = defaultdict(lambda: 0)
    for pos, color in floor.items():
        if color == 0:
            for d in DELTA.values():
                count[move(pos, d)] += 1

    floor1 = defaultdict(lambda: 1)

    for pos, color in floor.items():
        if color == 0 and count[pos] == 1:
            floor1[pos] = 0

    for pos, cnt in count.items():
        if cnt == 2:
            floor1[pos] = 0

    return floor1


def solve2(floor):
    for i in range(100):
        floor = flip(floor)
    return count_black_tiles(floor)


def count_black_tiles(floor):
    return len([tile for tile in floor.values() if tile == 0])


def main(inp):
    steps_list = read_input(inp)
    floor = make_floor(steps_list)
    print("part 1", solve1(floor))
    print("part 2", solve2(floor))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)