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


def parse(line):
    head, rest = line.split(':')
    head = int(head.strip())
    rest = list(map(int, rest.split()))
    return head, rest


def concat(a, b):
    return int(str(a) + str(b))


def can_reach(goal:int, nums: list[int], allow_concat = False):
    acc = {nums[0]}
    for i in range(1, len(nums)):
        new_acc = set()
        for a in acc:
            a1 = a + nums[i]
            if a1 <= goal:
                new_acc.add(a1)
            a2 = a * nums[i]
            if a2 <= goal:
                new_acc.add(a2)
            if allow_concat:
                a3 = concat(a, nums[i])
                if a3 <= goal:
                    new_acc.add(a3)
        acc = new_acc
    return acc


def solve1(lines, allow_concat = False):
    tot = 0
    for line in lines:
        goal, nums = parse(line)
        reach = can_reach(goal, nums, allow_concat=allow_concat)
        if goal in reach:
            tot += goal
    return tot


def main(argv):
    lines = get_lines()
    print("part 1")
    print(solve1(lines))
    print()
    print("part 2")
    print(solve1(lines, allow_concat=True))


if __name__ == '__main__':
    main(sys.argv)
