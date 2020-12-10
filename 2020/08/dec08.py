import sys

prog = []
for line in sys.stdin:
    x, y = line.strip().split()
    prog.append((x.strip(), int(y.strip())))


def next(prog, pc):
    x, y = prog[pc]
    if x == 'jmp':
        return pc + y
    else:
        return pc + 1


def other(op):
    if op == 'jmp':
        return 'nop'
    elif op == 'nop':
        return 'jmp'
    else:
        return op


def run(prog):
    seen = set()
    pc = 0
    acc = 0

    while pc not in seen and pc < len(prog):
        seen.add(pc)
        x, y = prog[pc]
        pc = next(prog, pc)
        if x == 'acc':
            acc += y
    return acc, pc


# part 1
print("part 1:", run(prog)[0])


# part 2
pos = 0
while True:
    x, y = prog[pos]
    prog[pos] = (other(x), y)
    acc, pc = run(prog)
    prog[pos] = (x, y)
    pos += 1
    if (pc == len(prog)):
        print("part 2:", acc)
        break
