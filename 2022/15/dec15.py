import re
import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


pattern = re.compile('Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)')


def get_coords(line: str):
    m = pattern.match(line)
    n = [int(m.group(i)) for i in range(1, 5)]
    return (n[0], n[1]), (n[2], n[3])


def get_all_coords(lines: list):
    return [get_coords(line) for line in lines]


def dist(p, q):
    x, y = p
    v, w = q
    return abs(x - v) + abs(y - w)


def add_interval(intervals: set, x1: int, x2: int):
    ints = set()
    for (x3, x4) in intervals:
        if x1 > x4 + 1 or x2 < x3 - 1:
            ints.add((x3, x4))
        else:
            x1 = min(x1, x3)
            x2 = max(x2, x4)
    ints.add((x1, x2))
    return ints


def cover(sensor, d, y):
    sx, sy = sensor
    dx = d - abs(sy - y)
    return sx - dx, sx + dx


if __name__ == '__main__':

    file_name = sys.argv[1]
    with open(file_name) as f:
        all_coords = get_all_coords(get_lines(f))

    sensors = dict()
    beacons = set()
    for p, q in all_coords:
        beacons.add(q)
        sensors[p] = dist(p, q)

    print("part 1")
    y = 10 if file_name.endswith('sample') else 2000000
    ints = set()
    beacon_or_sensor = set()
    if y % 1000 == 0:
        print("y =", y)
    for (sx, sy) in sensors:
        if sy  == y:
            ints = add_interval(ints, sx, sx)
            beacon_or_sensor.add(sx)
    for bx, by in beacons:
        if by == y:
            ints = add_interval(ints, bx, bx)
            beacon_or_sensor.add(bx)
    for s, d in sensors.items():
        x1, x2 = cover(s, d, y)
        if x1 <= x2:
            ints = add_interval(ints, x1, x2)
    nblocked = 0
    for (x1, x2) in ints:
        nblocked += 1 + x2 - x1
    nblocked -= len(beacon_or_sensor)
    print(nblocked)
#    blocked = set()
#    for s, d in sensors.items():
#        x1, x2 = cover(s, d, y)
#        if x1 > x2:
#            continue
#        for x in range(x1, x2 + 1):
#            if (x,y) not in sensors and (x, y) not in beacons:
#                blocked.add((x,y))
#    print(sorted(blocked))
#    print(len(blocked))


    print()
    print("part 2")
    xmin, ymin = 0, 0
    xmax, ymax = 20, 20 if file_name.endswith('sample') else 4000000
    for y in range(ymin, ymax + 1):
        ints = set()
        if y % 100000 == 0:
            print("y =", y)
        for (sx, sy) in sensors:
            if sy  == y:
                ints = add_interval(ints, sx, sx)
        for bx, by in beacons:
            if by == y:
                ints = add_interval(ints, bx, bx)
        for s, d in sensors.items():
            x1, x2 = cover(s, d, y)
            if x1 <= x2:
                ints = add_interval(ints, x1, x2)
        if len(ints) > 1:
            print(y, ints)
            [(x1, x2), (x3, x4)] = ints
            print((x2 + 1) * 4000000 + y)
            print("^^^^^")
        else:
            [(x1, x2)] = ints
            if x1 > xmin or x2 < xmax:
                print(y, ints)
                print("^^^^^")
                raise Exception("We have assumed this does not happen")


