import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_op(line: str):
    # noop
    if line.startswith('noop'):
        return ('noop', 0, 1)
    else:
        # addx
        n = int(line.split()[1].strip())
        return ('addx', n, 2)


def get_ops(lines):
    return [get_op(line) for line in lines]


def do_run(ops):
    r = []
    x = 1
    cycle = 0
    for op in ops:
        opcode, val, cycles = op
        assert opcode in ['addx', 'noop']
        for i in range(cycles):
            cycle += 1
            r.append((cycle, x))
        x += val
    return r


def draw(run):
    col = 0
    for c, x in run:
        if col in {x - 1, x + 1, x}:
            sys.stdout.write('#')
        else:
            sys.stdout.write('.')
        col += 1
        if col == 40:
            print()
            col = 0
    print()


def main():
    lines = get_lines()
    ops = get_ops(lines)

    run = do_run(ops)

    print("part 1")
    # 20th, 60th, 100th, 140th, 180th, and 220th
    s = 0
    for cycle, x in run:
        if cycle in [20, 40, 60, 100, 140, 180, 220]:
            s += cycle * x
    print(s)

    print()
    print("part 2")
    draw(run)


if __name__ == '__main__':
    main()
