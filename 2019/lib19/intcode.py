import collections

class OpCode(object):
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    JPT = 5
    JPF = 6
    LTE = 7
    EQU = 8
    BSE = 9
    STP = 99

class Mode(object):
    POS = 0
    IMD = 1
    REL = 2


def read_prog(inp):
    line = inp.readline()
    while line:
        yield [int(x) for x in line.strip().split(',')]
        line = inp.readline()


def addr(a, mode, base):
    if mode == Mode.POS:
        return a
    if mode == Mode.REL:
        return base + a
    raise Exception("Illegal mode: " + str(mode))


def val(mem, x, m, base):
    if m == Mode.IMD:
        return x
    else:
        return mem[addr(x, m, base)]


def fetch_params(mem, pc, num):
    return [mem[pc + 1 + i] for i in range(num)]


def parse_op(xop):
    op = xop % 100
    m1 = (xop // 100) % 10
    m2 = (xop // 1000) % 10
    m3 = (xop // 10000) % 10
    return op, (m1, m2, m3)


def step(mem, pc, inp, base):
    op, (m1, m2, m3) = parse_op(mem[pc])

    if op == OpCode.ADD:
        npars = 3
        p1, p2, p3 = fetch_params(mem, pc, npars)
        mem[addr(p3, m3, base)] = val(mem, p1, m1, base) + val(mem, p2, m2, base)
        return base, pc + npars + 1, None
    elif op == OpCode.MUL:
        npars = 3
        p1, p2, p3 = fetch_params(mem, pc, npars)
        mem[addr(p3, m3, base)] = val(mem, p1, m1, base) * val(mem, p2, m2, base)
        return base, pc + npars + 1, None
    elif op == OpCode.INP:
        npars = 1
        p1, = fetch_params(mem, pc, npars)
        a = addr(p1, m1, base)
        mem[a] = next(inp)
        return base, pc + npars + 1, None
    elif op == OpCode.OUT:
        npars = 1
        p1, = fetch_params(mem, pc, npars)
        #        p1 = mem[addr(m1, base, pc + 1)]
        return base, pc + npars + 1, val(mem, p1, m1, base)
    elif op == OpCode.JPT:
        npars = 2
        p1, p2 = fetch_params(mem, pc, npars)
        if val(mem, p1, m1, base) != 0:
            return base, val(mem, p2, m2, base), None
        return base, pc + npars + 1, None
    elif op == OpCode.JPF:
        npars = 2
        p1, p2 = fetch_params(mem, pc, npars)
        if val(mem, p1, m1, base) == 0:
            return base, val(mem, p2, m2, base), None
        return base, pc + npars + 1, None
    elif op == OpCode.LTE:
        npars = 3
        p1, p2, p3 = fetch_params(mem, pc, npars)
        addr1 = addr(p3, m3, base)
        if val(mem, p1, m1, base) < val(mem, p2, m2, base):
            mem[addr1] = 1
        else:
            mem[addr1] = 0
        return base, pc + npars + 1, None
    elif op == OpCode.EQU:
        npars = 3
        p1, p2, p3 = fetch_params(mem, pc, npars)
        addr2 = addr(p3, m3, base)
        if val(mem, p1, m1, base) == val(mem, p2, m2, base):
            mem[addr2] = 1
        else:
            mem[addr2] = 0
        return base, pc + npars + 1, None
    elif op == OpCode.BSE:
        npars = 1
        p1, = fetch_params(mem, pc, npars)
        base += val(mem, p1, m1, base)
        return base, pc + npars + 1, None
    elif op == 99:
        return base, pc, None
    else:
        raise Exception("illegal op " + op)


def run(prog, inp, pc=0):
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

    # for problem 15, yield initial position as first step!
    yield mem, None, 0, mem[pc] != 99
    while mem[pc] != 99:
        base, pc, out = step(mem, pc, inp, base)
        yield mem, out, pc, True
    while True:
        yield mem, None, pc, False
# ----
