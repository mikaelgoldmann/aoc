import sys


def read_prog(inp):
    line = inp.readline()
    while line:
        yield [int(x) for x in line.strip().split(',')]
        line = inp.readline()


def val(mem, x, m):
    if m == 1:
        return x
    elif m == 0:
        return mem[x]
    else:
        raise Exception("illegal mode " + m)
        


def step(mem, pc, inp):
    xop = mem[pc]
    op = xop % 100
    m1 = (xop // 100) % 10
    m2 = (xop // 1000) % 10
    m3 = (xop // 10000) % 10
    assert m3 == 0
    
    if op == 1:
        # add
        p1, p2, p3 = mem[pc+1 : pc+4]
        mem[p3] = val(mem, p1, m1) + val(mem, p2, m2)
        return pc + 4, None
    elif op == 2:
        # mul
        p1, p2, p3 = mem[pc+1 : pc+4]
        mem[p3] = val(mem, p1, m1) * val(mem, p2, m2)
        return pc + 4, None
    elif op == 3:
        # input
        a = mem[pc + 1]
        mem[a] = next(inp)
        return pc + 2, None
    elif op == 4:
        # output
        p1 = mem[pc + 1]
        return pc + 2, val(mem, p1, m1)
    elif op == 5:
        # jump-if-true
        p1, p2 = mem[pc+1: pc+3]
        if val(mem, p1, m1) != 0:
            return val(mem, p2, m2), None
        return pc + 3, None
    elif op == 6:
        # jump-if-false
        p1, p2 = mem[pc+1: pc+3]
        if val(mem, p1, m1) == 0:
            return val(mem, p2, m2), None
        return pc + 3, None
    elif op == 7:
        # less-than
        p1, p2, p3 = mem[pc+1 : pc+4]
        if val(mem, p1, m1) < val(mem, p2, m2):
            mem[p3] = 1
        else:
            mem[p3] = 0
        return pc + 4, None
    elif op == 8:
        # equal-to
        p1, p2, p3 = mem[pc+1 : pc+4]
        if val(mem, p1, m1) == val(mem, p2, m2):
            mem[p3] = 1
        else:
            mem[p3] = 0
        return pc + 4, None
    elif op == 99:
        return pc, None
    else:
        raise Exception("illegal op " + op)



def run(mem, inp, pc):
    """
    mem: initial memory config (parameter not modified)
    inp: iterator of inputs
    pc: start program counter

    Runs one step
    Returns: memory contents (internal state), output or None, next pc, bool running (False if last op was 99)
    """
    out = []
    mem = mem[:]
    while mem[pc] != 99:
        pc, out = step(mem, pc, inp)
        yield mem, out, pc, True
    while True:
        yield mem, None, pc, False
