from dataclasses import dataclass, field
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

    def __str__(self):
        return """
        A: %d, %d
        B: %d, %d
        P: %d, %d
        """ % (self.a[0], self.a[1], self.b[0], self.b[1], self.prize[0], self.prize[1])


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


def eval2(test_case):
    xa, ya = test_case.a
    xb, yb = test_case.b
    xp, yp = test_case.prize
    # / xa xb \  / u \  = / xp \
    # \ ya yb /  \ v /    \ yp /
    dprint(test_case)
    det = (xa * yb) - (ya * xb)
    if det == 0:
        # degenerate case... zero or infinite solutions
        # if infinite, find cheapest
        dprint("singular")
        raise NotImplemented("Singular matrix")
    else:
        # normal case, solve and check that it is a legal, integer solution
        # inverse is
        #
        # det^(-1)  /  yb -xb \
        #           \ -ya  xa /
        dprint("non-singular")
        u1 = yb * xp - xb * yp
        v1 = xa * yp - ya * xp
        dprint(u1 * xa,  v1 * xb, xp, det)
        assert u1 * xa + v1 * xb == xp * det
        dprint(u1, v1, det)
        if u1 % det != 0:
            return 0
        if v1 % det != 0:
            return 0
        u = u1 // det
        v = v1 // det
        dprint(u, v)
        if u < 0 or v < 0:
            return 0
        return 3 * u + v


def solve2(test_cases):
    acc = 0
    for i, t in enumerate(test_cases):
        acc += eval2(t)
        dprint(i)
    return acc


def main(the_file):
    test_cases = [parse_test(p) for p in get_paragraphs(the_file)]
    print("part 1")
    print(solve2(test_cases))
    print()
    print("part 2")
    TERM = 10000000000000
    test_cases2 = [Test(t.a, t.b, (t.prize[0] + TERM, t.prize[1] + TERM)) for t in test_cases]
    print(solve2(test_cases2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true', default=False)
    parser.add_argument("--file", default=None)
    args = parser.parse_args(sys.argv[1:])
    DEBUG = args.debug
    print(DEBUG)
    if args.file:
        with open(args.file) as inp:
            main(inp)
    else:
        main(sys.stdin)
