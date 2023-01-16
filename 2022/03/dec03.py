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


def prio(x):
    if x >= 'a':
        return 1 + ord(x) - ord('a')
    return 27 + ord(x) - ord('A')


lines = get_lines()

print("part 1", None)
s = 0
for l in lines:
    n = len(l) // 2
    a = l[:n]
    b = l[n:]
    x = set(a).intersection(set(b)).pop()
    s += prio(x)
print(s)


print("part 2", None)
s = 0
for i in range(0, len(lines), 3):
    a, b, c = tuple(map(set, (lines[i], lines[i+1], lines[i+2])))
    x = a.intersection(b).intersection(c).pop()
    s += prio(x)
print(s)
