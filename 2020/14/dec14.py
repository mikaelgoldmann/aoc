import sys
import re


MEM_RE = re.compile('mem\[([0-9]+)\] = ([0-9]+)')
MASK_RE = re.compile('mask = ([01X]+)')

def parse(x):
    mmem = MEM_RE.fullmatch(x)
    mmsk = MASK_RE.fullmatch(x)
    assert mmem or mmsk
    if mmem:
        addr = int(mmem.group(1))
        val = int(mmem.group(2))
        return ('mem', (addr, val))
    else:
        return ('mask', mmsk.group(1))


def get_mask(val):
    xs = 0
    ys = 0
    for v in val:
        xs *= 2
        ys *= 2
        xs += 1 if v == 'X' else 0
        ys += 1 if v == '1' else 0
    return (xs, ys)


ops = [parse(x.strip()) for x in sys.stdin]

mask = 'X' * 32
mem = {}

for (op, pars) in ops:
    if op == 'mask':
        mask = get_mask(pars)
    else:
        addr, val = pars
        mem[addr] = (val & mask[0]) | mask[1]
#    print(mem)

part1 = sum(mem.values())


print("part 1", part1)


def addresses(mask, addr):
    addrs = [addr]
    for i in range(36):
        mbit = mask[35 - i]
        addrs2 = []
        for a in addrs:
            if mbit == '0':
                addrs2.append(a)
            elif mbit == '1':
                if not (a & (2 ** i)):
                    a += (2 ** i)
                addrs2.append(a)
            else:  # 'X'
                if not (a & (2 ** i)):
                    a2 = a + (2 ** i)
                else:
                    a2 = a - (2 ** i)
                addrs2.extend([a, a2])
        addrs = addrs2
    return addrs


mask = '0' * 32
mem = {}

for (op, pars) in ops:
    if op == 'mask':
        mask = pars
    else:
        addr, val = pars
        for a in addresses(mask, addr):
            mem[a] = val
#    print(mem)

part2 = sum(mem.values())

print("part 2", part2)
