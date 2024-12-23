import sys
from collections import  defaultdict


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


def solve1(lines):
    l1, l2 = split_lines(lines)
    xs = zip(l1, l2)
    s = 0
    for a, b in xs:
        s += abs(a - b)
    return s


def solve2(lines):
    l1, l2 = split_lines(lines)
    d = defaultdict(lambda: 0)
    for x in l2:
        d[x] += 1
    s = 0
    for x in l1:
        s += x * d[x]
    return s


def split_lines(lines):
    l1 = sorted(map(int, [x.split()[0].strip() for x in lines]))
    l2 = sorted(map(int, [x.split()[1].strip() for x in lines]))
    return l1, l2


def main(argv):
    print("part 1")
    with open('dec01.in') as f1:
        lines = get_lines(f1)
    print(solve1(lines))

    print()
    print("part 2")
    print(solve2(lines))


if __name__ == '__main__':
    main(sys.argv)
