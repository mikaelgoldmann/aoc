import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x[:-1] for x in f]

def get_paragraphs(lines=None):
    if lines is None:
        lines = get_lines()
    paragraph = []
    for x in lines:
        if not x:
            yield paragraph
            paragraph = []
        else:
            paragraph.append(x)
    if paragraph:
        yield paragraph


def get_stacks(start: list):
    n = len(start[-1].strip().split())
    stacks = [[] for i in range(n)]
    del(start[-1])
    while start:
        last = start[-1]
        del(start[-1])
        for i in range(n):
            x = last[:4].strip()
            last = last[4:]
            if (x):
                stacks[i].append(x[1])
    return stacks


def get_moves(moves):
    mv = []
    for move in moves:
        m, num, f, src, t, target = move.split()
        mv.append((int(num), int(src), int(target)))
    return mv


def perform(stacks, move):
    num, src, dst = move
    src = stacks[src-1]
    dst = stacks[dst-1]
    for i in range(num):
        dst.append(src.pop())


def perform2(stacks, move):
    num, src, dst = move
    src = stacks[src-1]
    dst = stacks[dst-1]
    x = []
    for i in range(num):
        x.append(src.pop())
    for i in range(num):
        dst.append(x.pop())


start, moves = get_paragraphs()
moves = get_moves(moves)


stacks = get_stacks(start)
stacks2 = []
for st in stacks:
    stacks2.append(st[:])

print("part 1", None)
for move in moves:
    perform(stacks, move)
for s in stacks:
    sys.stdout.write(s[-1])
print()

print()
print("part 2", None)
for move in moves:
    perform2(stacks2, move)
for s in stacks2:
    sys.stdout.write(s[-1])
print()
