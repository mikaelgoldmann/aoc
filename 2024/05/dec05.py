from collections import defaultdict
import sys
from pydoc import pager


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


def dfs(x, edges, num, mx):
    if num[x] > 0:
        return mx
    if num[x] == 0:
        raise Exception("Cyclic")
    num[x] = 0
    for y in edges[x]:
        if y in num:
            mx = dfs(y, edges, num, mx)
    num[x] = mx
    return mx -1


def top_sort(adj, pages):
    num = {}
    for p in pages:
        num[p] = -1
    mx = len(pages)
    for p in pages:
        mx = dfs(p, adj, num, mx)
    return num


def solve1(adj, jobs):
    s = 0
    for p in jobs:
        pages = list(map(int, p.split(',')))
        num = top_sort(adj, pages)
        if is_ok(num, pages):
            # print(pages)
            # print(ts)
            s += pages[len(pages) // 2]
    return s


def solve2(adj, jobs):
    s = 0
    for p in jobs:
        pages = list(map(int, p.split(',')))
        num = top_sort(adj, pages)
        if not is_ok(num, pages):
            pages.sort(key=lambda p1: num[p1])
            s += pages[len(pages) // 2]
    return s


def is_ok(num, pages):
    ts = [num[p] for p in pages]
    m = -1
    ok = True
    for t in ts:
        if t < m:
            ok = False
        m = t
    return ok


def get_edges(order):
    adj = defaultdict(set)
    for o in order:
        x, y = o.split('|')
        adj[int(x)].add(int(y))
    return adj


def main(argv):
    # sys.setrecursionlimit(1000000)
    order, jobs = list(get_paragraphs())
    edges = get_edges(order)
    print("part 1")
    print(solve1(edges, jobs))
    print()
    print("part 2")
    print(solve2(edges, jobs))


if __name__ == '__main__':
    main(sys.argv)
