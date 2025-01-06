import argparse
import re
import sys

from collections import defaultdict
from dataclasses import dataclass


DEBUG = False


ROBOT = re.compile('^p=([-]?[0-9]+),([-]?[0-9]+) v=([-]?[0-9]+),([-]?[0-9]+)$')


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def dprint(*a, **kw):
    if DEBUG:
        print(*a, **kw)


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


def step_robot(robot, width, height):
    robot.x += robot.dx
    robot.x %= width
    robot.y += robot.dy
    robot.y %= height


def step_robots(robots, width, height):
    for r in robots: step_robot(r, width, height)


def parse_robot(line):
    m = ROBOT.match(line)
    assert m
    return Robot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))


def solve(robots, width, height):
    steps = 100
    locations = defaultdict(lambda: 0)
    for r in robots:
        x = (r.x + steps * r.dx) % width
        y = (r.y + steps * r.dy) % height
        locations[(x, y)] += 1
    quads = [0, 0, 0, 0]
    midx = width  // 2
    midy = height // 2
    dprint(width, midx, height, midy)
    for (x, y), val in locations.items():
        dprint(x, y, val)
        if x < midx and y < midy:
            quads[0] += val
        elif x > midx and y < midy:
            quads[1] += val
        elif x < midx and y > midy:
            quads[2] += val
        elif x > midx and y > midy:
            quads[3] += val
        else:
            dprint("skipping", x, y, val)
    dprint(quads)
    acc = 1
    for q in quads:
        acc *= q
    return acc


def print_robots(robots, width, height):
    canvas = [ [' '] * width for h in range(height)]
    for r in robots:
        canvas[r.y][r.x] = '*'
    for row in canvas:
        print(''.join(row))


def tree_like(robots, width, height):
    distro = defaultdict(lambda: 0)
    for r in robots:
        distro[(r.x, r.y)] += 1
        if distro[(r.x, r.y)] > 1:
            return False
    prev = (-100, -100)
    acc = 0
    for pt in sorted(distro.keys()):
        if pt[0] == prev[0] and pt[1] == prev[1] + 1:
            acc += 1
        prev = pt
    return acc > 200


def find_tree(robots, width, height):
    for i in range(1000000):
        if tree_like(robots, width, height):
            print()
            print(i)
            print_robots(robots, width, height)
        step_robots(robots, width, height)
        if i % 10000 == 0: print(i)


def main(inp, width, height):
    robots = []
    lines = get_lines(inp)
    for line in lines:
        robots.append(parse_robot(line))
    print("part 1")
    print(solve(robots, width, height))
    print()
    print("part 2")
    robots = []
    for line in lines:
        robots.append(parse_robot(line))
    find_tree(robots, width, height)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true', default=False)
    parser.add_argument("--file", type=str)
    args = parser.parse_args(sys.argv[1:])
    DEBUG = args.debug
    is_sample = 'sample' in args.file
    width = 11 if is_sample else 101
    height = 7 if is_sample else 103
    with open(args.file) as inp:
        main(inp, width, height)
