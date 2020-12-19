import sys

mem = [int(x) for x in sys.stdin.readline().strip().split(',')]


def step(mem, pc):
    assert mem[pc] in [1, 2]
    op, p1, p2, p3 = mem[pc : pc+4]
    if op == 1:
        mem[p3] = mem[p1] + mem[p2]
    else:
        mem[p3] = mem[p1] * mem[p2]
    return pc + 4


def run(mem):
    mem = mem[:]
    pc = 0
    while mem[pc] != 99:
        pc = step(mem, pc)
        # print(mem)
    return mem

mem1 = mem[:]
mem1[1] = 12
mem1[2] = 2 
m = run(mem1)

print("step 1", m[0])

mem1 = mem[:]
for i in range(100):
    for j in range(100):
        mem[1] = i
        mem[2] = j
        if run(mem)[0] == 19690720:
            print("part 2", i * 100 + j)
