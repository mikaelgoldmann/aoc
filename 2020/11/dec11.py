import sys

def read():
    rows = [(['.'] + [y for y in x.strip()] + ['.']) for x in sys.stdin]
    sentinel = ['.'] * len(rows[0])
    return [sentinel] + rows + [sentinel]


def count(rows, i, j):
    s = 0
    for m in range(i-1, i +2):
        for n in range(j-1 , j+2):
            if n == j and m == i:
                continue
            if rows[m][n] == '#':
                s += 1
    return s


def copy(rows):
    return [ x[:] for x in rows]

def step(rows, count, limit):
    newrows = copy(rows)
    nr = len(rows)
    nc = len(rows[0])
    for r in range(1, nr -1):
        for c in range(1, nc-1):
            rc = rows[r][c]
            cnt = count(rows, r, c)
            if (rc == 'L') and cnt == 0:
                newrows[r][c] = '#'
            elif (rc == '#') and cnt >= limit:
                newrows[r][c] = 'L'
    return newrows
 

data = read()


def iterate(start, count, limit):
    newrows = copy(start)
    rows = []
    while rows != newrows:
        #    for x in newrows:
        #        print(x)
        rows = newrows[:]
        newrows = step(rows, count, limit)
    return rows

rows = iterate(data, count, 4)
s = 0
for r in rows:
    for c in r:
        if c == '#':
            s += 1

print("part 1", s)


def c2(rows, r, c, dr, dc):
    s = 0
    r += dr
    c += dc
    while r >=0 and r < len(rows) and c >= 0 and c < len(rows[0]):
        if rows[r][c] == '.':
            r += dr
            c += dc
        elif rows[r][c] == '#':
            return 1
        else:
            return 0
    return 0
            

def count2(rows, r, c):
    s = 0
    for dr in range(-1, 2):
        for dc in range(-1 , 2):
            if dr == 0  and dc == 0:
                continue
            s += c2(rows, r, c, dr, dc)
    return s


rows = iterate(data, count2, 5)
s = 0
for r in rows:
    for c in r:
        if c == '#':
            s += 1

print("part 2", s)
