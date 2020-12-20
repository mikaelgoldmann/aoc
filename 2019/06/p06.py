import sys

v = set()
p = {}


for line in sys.stdin:
    parent, child = line.strip().split(')')
    v.add(parent)
    v.add(child)
    p[child] = parent


def depth(u, p):
    if not u in p:
        return 0
    else:
        return 1 + depth(p[u], p)


s = 0
for u in v:
    s += depth(u, p)

print("part 1", s)


def path(u, p):
    x = []
    while u in p:
        x.append(p[u])
        u = p[u]
    return x


p1 = path('YOU', p)
p2 = path('SAN', p)

print(p1)
print(p2)

while p1[-2] == p2[-2]:
    p1.pop()
    p2.pop()

print(p1)
print(p2)

print("part2", len(p1) + len(p2) - 2)
