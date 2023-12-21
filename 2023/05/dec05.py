import sys


def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_paragraphs(lines=None) -> list[list[str]]:
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


def get_map(p: list[str]) -> list[tuple[int, int]]:
    assert ':' in p[0]
    return [tuple(x) for x in get_int_lines(p[1:])]


def map_value(map0: list[tuple[int, int]], s: int) -> int:
    for dst, src, n in map0:
        if src <= s < src + n:
            return dst + (s - src)
    return s


def interval_intersection(ivl1: tuple[int, int], ivl2: tuple[int, int]):
    """
    Find left, middle, right where
    * left is that part of ivl1 that is left of ivl2
    * middle is the intersection of ivl1 and ivl2
    * right is the part if ivl1 that is to the right of ivl2
    :param ivl1: (pos, len)
    :param ivl2: (pos, len)
    :return: left, middle, right
    """
    x1, m1 = ivl1
    x2, m2 = ivl2
    y1 = x1 + m1
    y2 = x2 + m2
    xlft, ylft = x1, min(y1, x2)
    left = (xlft, ylft - xlft)
    xmid, ymid = max(x1, x2), min(y1, y2)
    middle = (xmid, ymid - xmid)
    xrte, yrte = max(x1, y2), y1
    right = (xrte, yrte - xrte)
    return left, middle, right


def map_interval(map0: list[tuple[int, int]], ivls: list[tuple[int, int]]) -> list[tuple[int, int]]:
    mapped = []
    for dst, src, n in map0:
        unmapped = []
        for ivl in ivls:
            left, middle, right = interval_intersection(ivl, (src, n))
            if left[1] > 0:
                unmapped.append(left)
            if right[1] > 0:
                unmapped.append(right)
            if middle[1] > 0:
                m, mn = middle
                mapped.append((dst + m - src, mn))
        ivls = unmapped
    return mapped + ivls


def main(argv):
    lines = None
    if len(argv) == 2:
        with open(argv[1]) as f:
            lines = f.readlines()
    ps = [p for p in get_paragraphs(lines)]
    seeds = get_int_lines(ps[0])[0]
    maps = [get_map(p) for p in ps[1:]]
    print("part 1")
    pos = [x for x in seeds]
    for map0 in maps:
        pos = [map_value(map0, x) for x in pos]
    print(min(pos))

    print()
    print("part 2")
    intervals = []
    for i in range(0, len(seeds), 2):
        intervals.append(tuple(seeds[i:i+2]))
    for map0 in maps:
        # print (intervals)
        intervals = map_interval(map0, intervals)
    print(min(x for x,xm in intervals))


if __name__ == '__main__':
    main(sys.argv)
