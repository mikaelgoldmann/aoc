from collections import namedtuple
from dataclasses import dataclass, field
from heapq import heappop, heappush
import argparse
import re
import sys


BUTTON = re.compile("^Button [AB]: X[+]([0-9]+), Y[+]([0-9]+)$")
PRICE = re.compile("^Prize: X=([0-9]+), Y=([0-9]+)$")


@dataclass
class Test:
    a: (int, int)
    b: (int, int)
    prize: (int, int)


@dataclass(order=True)
class Node:
    x: int = field(compare=False)
    y: int = field(compare=False)
    d: int

    def is_valid(self, x, y):
        return self.x <= x and self.y <= y

    def is_goal(self, x, y):
        return self.x == x and self.y == y

    def add(self, dx, dy, dd):
        return Node(self.x + dx, self.y + dy, self.d + dd)

    def coord(self):
        return self.x, self.y


DEBUG = False


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


def parse_button(line):
    dprint('button', line)
    m = BUTTON.match(line)
    return int(m.group(1)), int(m.group(2))


def parse_prize(line):
    m = PRICE.match(line)
    return int(m.group(1)), int(m.group(2))


def parse_test(lines):
    button_line1, button_line2, prize_line = lines
    a = parse_button(button_line1)
    b = parse_button(button_line2)
    prize = parse_prize(prize_line)
    return Test(a, b, prize)


def eval1(test_case):
    xa, ya = test_case.a
    xb, yb = test_case.b
    px, py = test_case.prize
    q = [Node(0, 0, 0)]
    seen = set()
    while q:
        node = heappop(q)
        if node.is_goal(px, py):
            return node.d
        if node.coord() in seen:
            continue
        seen.add(node.coord())
        push_a = node.add(xa, ya, 3)
        if push_a.coord() not in seen and push_a.is_valid(px, py):
            heappush(q, push_a)
        push_b = node.add(xb, yb, 1)
        if push_b.coord() not in seen and push_b.is_valid(px, py):
            heappush(q, push_b)
    return 0

def solve1(test_cases):
    acc = 0
    for i, t in enumerate(test_cases):
        acc += eval1(t)
        print(i)
    return acc


def main(the_file):
    test_cases = [parse_test(p) for p in get_paragraphs(the_file)]
    print("part 1")
    print(solve1(test_cases))
    print()
    print("part 2")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true', default=False)
    parser.add_argument("--file", default=None)
    args = parser.parse_args(sys.argv[1:])
    DEBUG = args.debug
    if args.file:
        with open(args.file) as inp:
            main(inp)
    else:
        main(sys.stdin)
