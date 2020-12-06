import sys
from functools import reduce
from lib import paragraphs

# sol= 6457
# sol= 3260

cases = list(paragraphs(sys.stdin))

def combine(c, f):
    xs = [set(c1) for c1 in c]
    return list(reduce(f, xs))

def solve(cases, f):
    combs = [combine(c, f) for c in cases] 
    lens =[len(c) for c in combs]
    print("sol=", sum(lens))


#1
solve(cases, lambda x, y: x.union(y))

#2
solve(cases, lambda x, y: x.intersection(y))
