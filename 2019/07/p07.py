import sys
from itertools import permutations

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
        


def step(mem, pc, inp, out):
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
        return pc + 4
    elif op == 2:
        # mul
        p1, p2, p3 = mem[pc+1 : pc+4]
        mem[p3] = val(mem, p1, m1) * val(mem, p2, m2)
        return pc + 4
    elif op == 3:
        # input
        a = mem[pc + 1]
        mem[a] = next(inp)
        return pc + 2
    elif op == 4:
        # output
        p1 = mem[pc + 1]
        out.append(val(mem, p1, m1))
        return pc + 2
    elif op == 5:
        # jump-if-true
        p1, p2 = mem[pc+1: pc+3]
        if val(mem, p1, m1) != 0:
            return val(mem, p2, m2)
        return pc + 3
    elif op == 6:
        # jump-if-false
        p1, p2 = mem[pc+1: pc+3]
        if val(mem, p1, m1) == 0:
            return val(mem, p2, m2)
        return pc + 3
    elif op == 7:
        # less-than
        p1, p2, p3 = mem[pc+1 : pc+4]
        if val(mem, p1, m1) < val(mem, p2, m2):
            mem[p3] = 1
        else:
            mem[p3] = 0
        return pc + 4
    elif op == 8:
        # equal-to
        p1, p2, p3 = mem[pc+1 : pc+4]
        if val(mem, p1, m1) == val(mem, p2, m2):
            mem[p3] = 1
        else:
            mem[p3] = 0
        return pc + 4
    else:
        raise Exception("illegal op " + op)


def run(mem, inp):
    inp = iter(inp)
    out = []
    mem = mem[:]
    pc = 0
    while mem[pc] != 99:
        pc = step(mem, pc, inp, out)
        # print(mem)
    return mem, out

mems = []
for mem in read_prog(sys.stdin):
    mems.append(mem)


def run_amps(setting, mem):
    output = 0
    for i in range(5):
        inp = [setting[i], output]
        m, o = run(mem, inp)
        output = o[-1]
    return output


def solve1(mem):
    settings = list(permutations(range(5)))
    x = -1000000000
    for s in settings:
        x = max(x, run_amps(s, mem))
    return x
        

for mem in mems:
    print("step 1", solve1(mem))


