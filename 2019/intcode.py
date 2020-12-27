import collections


def read_prog(inp):
    line = inp.readline()
    while line:
        yield [int(x) for x in line.strip().split(',')]
        line = inp.readline()


def addr(mode, base, a):
    if mode == 0:
        return a
    if mode == 2:
        return base + a
    raise Exception("Illegal mode: " + str(mode))


def val(mem, x, m, base):
    if m == 1:
        return x
    elif m in [0, 2]:
        return mem[addr(m, base, x)]
    else:
        raise Exception("illegal mode [%d]" % m)


def fetch(mem, addrs):
    return [mem[a] for a in addrs]


def step(mem, pc, inp, base):
    xop = mem[pc]
    op = xop % 100
    m1 = (xop // 100) % 10
    m2 = (xop // 1000) % 10
    m3 = (xop // 10000) % 10

    if op == 1:
        # add
        p1, p2, p3 = fetch(mem, [pc + 1, pc + 2, pc + 3])
        mem[addr(m3, base, p3)] = val(mem, p1, m1, base) + val(mem, p2, m2, base)
        return base, pc + 4, None
    elif op == 2:
        # mul
        p1, p2, p3 = fetch(mem, [pc + 1, pc + 2, pc + 3])
        mem[addr(m3, base, p3)] = val(mem, p1, m1, base) * val(mem, p2, m2, base)
        return base, pc + 4, None
    elif op == 3:
        # input
        p1, = fetch(mem, [pc + 1])
        a = addr(m1, base, p1)
        mem[a] = next(inp)
        return base, pc + 2, None
    elif op == 4:
        # output
        p1, = fetch(mem, [pc + 1])
        #        p1 = mem[addr(m1, base, pc + 1)]
        return base, pc + 2, val(mem, p1, m1, base)
    elif op == 5:
        # jump-if-true
        p1, p2 = fetch(mem, [pc + 1, pc + 2])
        if val(mem, p1, m1, base) != 0:
            return base, val(mem, p2, m2, base), None
        return base, pc + 3, None
    elif op == 6:
        # jump-if-false
        p1, p2 = fetch(mem, [pc + 1, pc + 2])
        if val(mem, p1, m1, base) == 0:
            return base, val(mem, p2, m2, base), None
        return base, pc + 3, None
    elif op == 7:
        # less-than
        p1, p2, p3 = fetch(mem, [pc + 1, pc + 2, pc + 3])
        if val(mem, p1, m1, base) < val(mem, p2, m2, base):
            mem[addr(m3, base, p3)] = 1
        else:
            mem[addr(m3, base, p3)] = 0
        return base, pc + 4, None
    elif op == 8:
        # equal-to
        p1, p2, p3 = fetch(mem, [pc + 1, pc + 2, pc + 3])
        if val(mem, p1, m1, base) == val(mem, p2, m2, base):
            mem[addr(m3, base, p3)] = 1
        else:
            mem[addr(m3, base, p3)] = 0
        return base, pc + 4, None
    elif op == 9:
        p1 = mem[pc + 1]
        base += val(mem, p1, m1, base)
        return base, pc + 2, None
    elif op == 99:
        return base, pc, None
    else:
        raise Exception("illegal op " + op)


def run(prog, inp, pc):
    """
    mem: initial memory config (parameter not modified)
    inp: iterator of inputs
    pc: start program counter

    Runs one step
    Returns: memory contents (internal state), output or None, next pc, bool running (False if last op was 99)
    """
    out = []
    mem = collections.defaultdict(lambda: 0)
    mem.update(enumerate(prog))
    base = 0

    while mem[pc] != 99:
        base, pc, out = step(mem, pc, inp, base)
        yield mem, out, pc, True
    while True:
        yield mem, None, pc, False
# ----
