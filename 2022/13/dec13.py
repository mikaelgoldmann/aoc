import sys
from functools import cmp_to_key


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


def parse_pair(p):
    a,b = p
    assert a != b
    return eval(a), eval(b)


def cmp(a, b):
    if a == b:
        return 0
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int and type(b) == list:
        return cmp([a], b)
    if type(a) == list and type(b) == int:
        return cmp(a, [b])
    assert type(a) == list and type(b) == list
    if not a:
        return -1
    if not b:
        return 1
    c = cmp(a[0], b[0])
    if c == 0:
        c = cmp(a[1:], b[1:])
    return c




if __name__ == '__main__':
    ps = get_paragraphs()
    pairs = [parse_pair(p) for p in ps]
    print(pairs)

    s = 0
    for i, p in enumerate(pairs):
        if cmp(p[0], p[1]) < 0:
            s += (i + 1)

    print("part 1")
    print(s)

    print()
    all = []
    for a, b in pairs:
        all.extend([a, b])
    all.append([[2]])
    all.append([[6]])
    all = sorted(all, key=cmp_to_key(cmp))
    p = 1
    for i, x in enumerate(all):
        if x in [[[2]], [[6]]]:
            p *= (i + 1)
        print(x)
    print("part 2")
    print(p)
