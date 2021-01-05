import math
import sys


class Item(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count
    @staticmethod
    def parse(s):
        c, n = s.split()
        return Item(n.strip(), int(c.strip()))


class Rule(object):
    def __init__(self, product, ingredients):
        self.product = product
        self.ingredients = ingredients

    @staticmethod
    def parse(s):
        lft, rte = s.split('=>')
        product = Item.parse(rte.strip())
        ings = [Item.parse(i.strip()) for i in lft.split(',')]
        return Rule(product, ings)


def read_rules(inp):
    rs = [Rule.parse(r.strip()) for r in inp]
    items = [(r.product.name, r) for r in rs]
    assert len(set([i[0] for i in items])) == len(items)
    return dict(items)


def top_sort1(g, u, top_num, n):
    ings = g[u].ingredients
    for ing in ings:
        w = ing.name
        if w not in top_num and w != 'ORE':
            n = top_sort1(g, w, top_num, n)
    top_num[u] = n
    return n + 1


def top_sort(g, u):
    top_num = {}
    top_sort1(g, u, top_num, 0)
    items = sorted(top_num.items(), key=lambda i: -i[1])
    return [i[0] for i in items]


def solve1(rules, ordered, fuel=1):
    need = dict((i, 0) for i in ordered)
    need['FUEL'] = fuel
    need['ORE'] = 0
    for name in ordered:
        if need[name] == 0:
            continue
        rule = rules[name]
        prod = rule.product
        ings = rule.ingredients
        mult = math.ceil(need[name] / prod.count)
        for ing in ings:
            need[ing.name] += mult * ing.count
    return need['ORE']


def solve2(rules, ordered):
    lo = 0
    hi = 1
    oremax = 1000000000000
    while solve1(rules, ordered, hi) <= oremax:
        hi *= 2
    print("hi", hi)
    # lo < hi, solve1(..., lo) <= oremax < solve1(...,hi)
    while lo < hi - 1:
        m = (lo + hi) // 2
        if solve1(rules, ordered, m) <= oremax:
            lo = m
        else:
            hi = m
        print(lo, hi)
    return lo

def main(inp):
    rules = read_rules(inp)
    print(rules)
    ordered = top_sort(rules, "FUEL")
    print(ordered)
    print("step 1", solve1(rules, ordered))
    print("step 2", solve2(rules, ordered))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)
