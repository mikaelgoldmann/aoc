import sys


def parse(x):
    return x


lines = [parse(x.strip()) for x in sys.stdin]


tab = {
    ('A', 'A'): 3,
    ('A', 'B'): 6,
    ('A', 'C'): 0,
    ('B', 'A'): 0,
    ('B', 'B'): 3,
    ('B', 'C'): 6,
    ('C', 'A'): 6,
    ('C', 'B'): 0,
    ('C', 'C'): 3
}

tab2 = {
    'A': 1, 'B':2, 'C': 3
}

trans = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

def trans2(x, outcome):
    if outcome == 'X': # lose
        if x == 'A': return 'C'
        if x == 'B': return 'A'
        if x == 'C': return 'B'
    if outcome == 'Y': return x  # draw
    if outcome == 'Z': # win
        if x == 'A': return 'B'
        if x == 'B': return 'C'
        if x == 'C': return 'A'

print("part 1", None)
s = 0
for l in lines:
    x, y = l.split()
    y = trans[y]
    print (tab[(x,y)], tab2[y])
    s += tab[(x,y)] + tab2[y]
print(s)

print("part 2", None)
s = 0
for l in lines:
    x, y = l.split()
    y = trans2(x, y)
    print (tab[(x,y)], tab2[y])
    s += tab[(x,y)] + tab2[y]
print(s)
