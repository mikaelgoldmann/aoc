import sys


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



def parse(line):
    a, b = line.split(',')
    x = tuple( map(int,a.split('-')))
    y = tuple( map(int,b.split('-')))
    return (x,y)


def c(a, b):
    a1, a2 = a
    b1, b2 = b
    return a1 <= b1 and a2 >= b2


def c2(a, b):
    return c(a,b) or c(b,a)


def no_overlap(a, b):
    a1, a2 = a
    b1, b2 = b
    return a2 < b1 or b2 < a1


data = list(map(parse, get_lines()))


print("part 1", None)
s = 0
for a,b in data:
    if (c2(a,b)): s += 1
print(s)


print("part 2", None)
s = 0
for a,b in data:
    if not no_overlap(a,b): s += 1
print(s)
