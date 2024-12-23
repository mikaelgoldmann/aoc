import re
import sys
from pickle import encode_long

MUL = 'mul[(]([0-9]{1,3}),([0-9]{1,3})[)]'

PATTERN = re.compile(MUL)
PATTERN2 = re.compile(MUL + "|do[(][)]|don\'t[(][)]")


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def solve1(lines):
    s = 0
    for line in lines:
        for m in PATTERN.finditer(line):
            s += int(m.group(1)) * int(m.group(2))
    return s


def solve2(lines):
    s = 0
    enabled = True
    for line in lines:
        for m in PATTERN2.finditer(line):
            print(m.group(0))
            if "don't" in m.group(0):
                enabled = False
            elif "do" in m.group(0):
                enabled = True
            elif enabled:
                s += int(m.group(1)) * int(m.group(2))
    return s


def main(argv):
    lines = get_lines()
    print("part 1")
    print(solve1(lines))
    print()
    print("part 2")
    print(solve2(lines))


if __name__ == '__main__':
    main(sys.argv)
