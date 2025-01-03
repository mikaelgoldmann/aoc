from collections import OrderedDict
from collections import defaultdict
import heapq
import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_paragraphs(lines=None):
    if lines is None:
        lines = get_lines()
    paragraph = []
    for x in lines:
        x = x.strip()
        if not x:
            yield paragraph
            paragraph = []
        else:
            paragraph.append(x)
    if paragraph:
        yield paragraph


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


def parse_line(line):
    mem = []
    id1 = 0
    for i, c in enumerate(line):
        if i % 2 == 0:
            for j in range(int(c)):
                mem.append(id1)
            id1 += 1
        else:
            for j in range(int(c)):
                mem.append('.')
    return mem


def rearrange1(mem):
    i = 0
    j = len(mem) - 1
    # print(mem)
    while i < j:
        if mem[i] == '.' and mem[j] != '.':
            mem[i] = mem[j]
            mem[j] = '.'
            # print(mem)
        if mem[i] != '.':
            i += 1
        if mem[j] == '.':
            j -= 1


def parse_line2(line):
    free = defaultdict(list)

    content = []
    pos = 0
    for i, n in enumerate(line):
        n = int(n)
        if i % 2 == 0:
            content.append((i // 2, pos, n))
        else:
            free[n].append(pos)
        pos += n
    return content, free


def rearrange2(mem, content, free):
    for id1, pos, n in reversed(content):
        free_size = pos
        start = 2 ** 30
        for m in range(n, 10):
            if free[m] and free[m][0] < start:
                free_size = m
                start = free[m][0]
        if start < pos:
            free_pos  = heapq.heappop(free[free_size])
            assert free_pos == start
            for i in range(n):
                mem[start + i] = id1
                mem[pos + i] = '.'
            heapq.heappush(free[free_size - n], start + n)


def check_sum(mem):
    acc = 0
    for i, v in enumerate(mem):
        if v != '.':
            acc += i * v
    return acc


def main(argv):
    line = get_lines()[0]
    print("part 1")
    mem = parse_line(line)
    mem1 = mem[:]
    rearrange1(mem1)
    print(check_sum(mem1))
    print()
    print("part 2")
    mem2 = mem[:]
    content, free = parse_line2(line)
    rearrange2(mem2, content, free)
    print(check_sum(mem2))


if __name__ == '__main__':
    main(sys.argv)
