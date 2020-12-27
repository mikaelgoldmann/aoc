import sys


ncols, nrows = list(map(int, sys.argv[1:3]))

image = sys.stdin.readline().strip()

assert len(image) % (ncols * nrows) == 0

layers = []
for i in range(0, len(image), ncols * nrows):
    layers.append(image[i:i+ncols*nrows])


def cnt(x, layer):
    return len([y for y in layer if y == x])


l1 = None
m = 2 ** 100
for l2 in layers:
    m2 = cnt('0', l2)
    if m2 < m:
        m = m2
        l1 = l2

print("part 1", cnt('1', l1) * cnt('2', l1))


out = [2] * (ncols * nrows)

for l1 in layers:
    for i in range(len(l1)):
        if out[i] == 2:
            out[i] = int(l1[i])

for r in range(nrows):
    for c in range(ncols):
        sys.stdout.write('X' if out[r * ncols + c] == 1 else ' ')
    print()

print()
for c in out:
    sys.stdout.write(str(c))

print()

