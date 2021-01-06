import sys


PATTERN = [0, 1, 0, -1]


def val(r, c):
    j = ((c + 1) // (r + 1)) % 4
    return PATTERN[j]


def row(n, i):
    return [val(i, j) for j in range(n)]


def dotprod(u, v):
    return sum(x * y for x, y in zip(u, v))


def mul(m, v):
    return [dotprod(m[i], v) for i in range(len(m))]


def truncate(v):
    def trunc(x):
        if x < 0:
            x = -x
        return x % 10
    return [trunc(x) for x in v]


def matrix(n):
    rows = []
    for i in range(n):
        r = row(n, i)
        rows.append(r)
    return rows


def phase(m, v):
    return truncate(mul(m, v))


def run(m, v, times, do_print=False):
    while times:
        print("times", times)
        v = phase(m, v)
        if do_print:
            print(v)
        times -= 1
    return v


def parse(data):
    return [int(x) for x in data]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        do_print = False
        times = 100
        with open(sys.argv[1]) as f:
            data = f.readline().strip()
    else:
        do_print = True
        times = 4
        data = '12345678'
    print(len(data))
    m = matrix(len(data))
    v = run(m, parse(data), times, do_print)[:8]
    print("step 1", ''.join(map(str, v)))
