import sys

D = dict(F=0, B=1, L=0, R=1)


def seat_id(r):
    i = 0
    for x in r:
        i *= 2
        i += D[x]
    return i


rows = [r.strip() for r in sys.stdin]

print("part 1:", max([seat_id(r) for r in rows]))

seat_ids = sorted([seat_id(r) for r in rows])

prev = -1000
for i in seat_ids:
    if i == prev + 2:
        print("part 2:", i - 1)
        break
    else:
        prev = i





