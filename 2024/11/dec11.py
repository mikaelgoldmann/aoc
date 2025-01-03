import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_int_lines(lines=None):
    if lines is None:
        lines = get_lines()
    int_lines = []
    for line in lines:
        int_line = []
        for x in line.split():
            try:
                x = int(x)
                int_line.append(x)
            except:
                pass
        int_lines.append(int_line)
    return int_lines


def ndigits(stone):
    n = 1
    d = 10
    while d <= stone:
        n += 1
        d *= 10
    return n


def blink(stone, blinks, mem):
    if blinks == 0:
        # sys.stdout.write("%d " % stone)
        return 1
    if (stone, blinks) in mem:
        return mem[(stone, blinks)]
    n = ndigits(stone)
    if stone == 0:
        r = blink(1, blinks - 1, mem)
    elif n % 2 == 1:
        r = blink(stone * 2024, blinks - 1, mem)
    else:
        half = 10 ** (n // 2)
        a = stone // half
        b = stone % half
        r = blink(a, blinks - 1, mem) + blink(b, blinks - 1, mem)
    mem[(stone, blinks)] = r
    return r



def solve1(stones, blinks=25):
    mem = {}
    acc = 0
    for stone in stones:
        acc += blink(stone, blinks, mem)
    return acc


def main(argv):
    stones = get_int_lines()[0]
    print("part 1")
    val1 = solve1(stones)
    print()
    print(val1)

    print()
    print("part 2")
    val1 = solve1(stones, blinks=75)
    print()
    print(val1)


if __name__ == '__main__':
    main(sys.argv)
