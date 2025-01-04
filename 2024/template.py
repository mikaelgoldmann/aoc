import sys
import argparse


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


def main(inp):
    print("part 1")
    print()
    print("part 2")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", type=bool, default=False)
    parser.add_argument("--file", type=str, default=None)
    args = parser.parse_args(sys.argv)
    DEBUG = args.debug
    if args.file:
        with open(args.file) as inp:
            main(inp)
    else:
        main(sys.stdin)
