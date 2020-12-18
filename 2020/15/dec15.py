import sys

#data = [int(x) for x in sys.stdin.readline().strip().split(',')]


def solve(data, length=2020):
    last = {}
    ns = []

    def add_num(n, pos, last):
        if n not in last:
            last[n] = [pos]
        else:
            last[n].append(pos)

    for pos, n in enumerate(data):
        if (pos % 1000000 == 0):
            print(pos)
        ns.append(n)
        add_num(n, pos, last)


    for pos in range(len(ns), length):
        if (pos % 1000000 == 0):
            print(pos)
        n = ns[-1]
        x = last[n]
        if len(x) == 1:
            next = 0
        else:
            next = x[-1] - x[-2]
        add_num(next, pos, last)
        ns.append(next)

    return ns

print(solve([0,3,6])[-1])  # 436
print(solve([2,3,1])[-1])  # 78
print("part 1", solve([1,17,0,10,18,11,6])[-1])  # 595
print("part 2", solve([1,17,0,10,18,11,6], 30000000)[-1])  # 1708310
