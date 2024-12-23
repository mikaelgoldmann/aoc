import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_report(line):
    return [int(x) for x in line.split()]


def get_reports(lines):
    return [get_report(line) for line in lines]


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


def is_safe(report: list[int], d: int, skip: int = -1) -> bool:
    # print(report)
    x = None
    for i,y in enumerate(report):
        if i == skip:
            continue
        # print(y)
        if x is not None and y not in [x + d, x + 2 * d, x + 3 * d]:
            # print(False)
            return False
        x = y
    #print(True)
    return True


def solve1(reports):
    return sum((int(is_safe(r, 1) or is_safe(r, -1)) for r in reports))


def solve2(reports):
    s = 0
    for r in reports:
        sfe = is_safe(r, 1) or is_safe(r, -1)

        for i in range(len(r)):
            if is_safe(r, 1, i) or is_safe(r, -1, i):
                sfe = True
        s += int(sfe)
    return s



def main(argv):
    print("part 1")
    lines = get_lines()
    reports = get_reports(lines)
    print(solve1(reports))
    print()
    print("part 2")
    print(solve2(reports))


if __name__ == '__main__':
    main(sys.argv)
