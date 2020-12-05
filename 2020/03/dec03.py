import sys

rows = [line.strip() for line in sys.stdin]
nrows = len(rows)
ncols = len(rows[0])

dr, dc = 1, 3
#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.

deltas = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

def trees(dc, dr):
    pr, pc= 0, 0
    ntrees = 0

    while pr < nrows:
        ntrees += 1 if rows[pr][pc] == '#' else 0
        pr += dr
        pc = (pc + dc) % ncols
    return ntrees

res = 1
for dc,dr in deltas:
    t = trees(dc, dr)
    print(dc, dr, t)
    res *= t

print(res)
