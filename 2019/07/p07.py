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
    out = []
    mem = mem[:]
    while mem[pc] != 99:
        pc, out = step(mem, pc, inp)
        yield mem, out, pc, True
    while True:
        yield mem, None, pc, False


# -------

from itertools import permutations

mems = []
for mem in read_prog(sys.stdin):
    mems.append(mem)


def run_99(m):
    res = None
    for mem, out, pc, running in m:
        print (len(mem), out, pc, running)
        if out is not None:
            res = out
        if not running:
            return res


def run_amps(setting, mem):
    output = 0
    for i in range(5):
        inp = iter([setting[i], output])
        m = run(mem, inp, 0)
        output = run_99(m)
    return output


def solve1(mem):
    settings = list(permutations(range(5)))
    x = -1000000000
    for s in settings:
        x = max(x, run_amps(s, mem))
    return x
        

def run_io_or_99(m):
    while True:
        mem, out, pc, running = next(m)
        if out is not None or not running:
            return out, running


def run_amps2(setting, mem):
    inp = [[s] for s in setting]
    m = [iter(run(mem, iter(i), 0)) for i in inp]
    output = 0
    outs = [None] * len(setting)
    M = len(setting)
    i = 0

    while True:
        inp[i].append(output)
        out, running = run_io_or_99(m[i])
        if out is not None:
            outs[i] = out
            output = out
        else:
            assert not running
        if not running:
            break
        i = (i + 1) % M
    return outs[-1]


def solve2(mem):
    settings = list(permutations(range(5,10)))
    x = -1000000000
    for s in settings:
        x = max(x, run_amps2(s, mem))
    return x
    


for mem in mems:
    print("step 1", solve1(mem))


for mem in mems:
    print("step 2", solve2(mem))


