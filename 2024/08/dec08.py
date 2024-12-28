from collections import defaultdict
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


def get_antinode(loc1, loc2, i=1):
    r1, c1 = loc1
    r2, c2 = loc2
    assert r1 != r2 or c1 != c2
    dr = r2 - r1
    dc = c2 - c1
    r3 = r2 + i * dr
    c3 = c2 + i * dc
    return r3, c3


def find_fq_antinodes(fq_locs, nrows, ncols, antinodes, start=1, end=1):
    for loc1 in fq_locs:
        for loc2 in fq_locs:
            if loc1 != loc2:
                i = start
                while True:
                    r, c = get_antinode(loc1, loc2, i=i)
                    if r < 0 or c < 0:
                        break
                    if r >= nrows or c >= ncols:
                        break
                    antinodes.add((r, c))
                    i += 1
                    if i > end:
                        break


def find_antinodes(locs: dict[str, list[str]], nrows: int, ncols: int, start=1, end=1):
    antinodes = set()
    for fq, fq_locs in locs.items():
        find_fq_antinodes(fq_locs, nrows, ncols, antinodes, start, end)
    return antinodes


def main(argv):
    lines = get_lines()
    locations = defaultdict(list)
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell != '.':
                locations[cell].append((row, col))
    print("part 1")
    print(len(find_antinodes(locations, len(lines), len(lines[0]))))
    print()
    print("part 2")
    print(len(find_antinodes(locations, len(lines), len(lines[0]), start=0, end=2 ** 1000)))


if __name__ == '__main__':
    main(sys.argv)
