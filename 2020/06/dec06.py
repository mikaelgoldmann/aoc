import sys
from functools import reduce

cases = [x for x in sys.stdin.read().strip().split("\n\n")]

def combine(c, f):
    xs = [set(c1) for c1 in c.split()]
    return list(reduce(f, xs))

def solve(cases, f):
    combs = [combine(c, f) for c in cases] 
    lens =[len(c) for c in combs]
    print("sol=", sum(lens))


#1
solve(cases, lambda x, y: x.union(y))

#2
solve(cases, lambda x, y: x.intersection(y))
