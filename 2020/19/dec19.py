import sys
from collections import defaultdict

def parse_line(x):
   x = x.strip()
   if not x:
       return None
   if ':' not in x:
       return ('string', x)
   x, rest = x.split(':')
   if '"' in rest:
       rest = rest.strip()
       assert len(rest) == 3
       return ("rule", (int(x), (rest[1],)))
   opts = tuple((y.strip().split()) for y in rest.split('|'))
   for o in opts:
       if len(o) > 2:
           print (len(o))
   return ('rule', (x, opts)) 


lines = [parse_line(x.strip()) for x in sys.stdin]
lines = [line for line in lines if line]

strings = [ y for x,y in lines if x == 'string'  ]
rules =  [ y for x,y in lines if x == 'rule'  ]


def split(n, k):
    if n < k:
        return []
    if k == 1:
        return [(n,)]
    res = []
    for i in range(1, n + 1):
        for s in split(n - i, k - 1):
            res.extend( [ (i,) + s ] )
    return res


def match1(i, j, sym, m):
    return sym in m[(i, j)]


def match(i, j, rhs, m):
    if i >= j:
        return False
    if len(rhs) == 1:
        return match1(i, j, rhs[0], m)
    sym = rhs[0]
    rhs = rhs[1:]
    for k in range(i + 1, j):
        if match1(i, k, sym, m) and match(k, j, rhs, m):
            return True
    return False


def parse(s, rs):
    m = defaultdict(lambda: set())
    r1 = dict([ (y[0][0], x) for x,y in rs if len(y) == 1 and len(y[0]) == 1 ])
    print(r1)
    for i in range(len(s)):
        assert s[i] in r1
        m[(i, i+1)].add(r1[s[i]])
    for k in range(2, len(s) + 1):
        for i in range(0, len(s)):
            if i + k > len(s):
                continue
            for lhs, opts in rs:
                for o in opts:
                    if match(i, i + k, o, m):
                        print (lhs, "generates", s[i:i+k])
                        m[(i, i + k)].add(lhs)
    return m


def gen2(x, s, i, j, mem, rules, rule):
    sym, rhs = rule
    if j <= i:
        return False
    for rh in rhs:
        if gen3(rhs, i, j, mem, rules)
        
        


def gen1(x, s, i, j, mem, rules):
    if j <= i:
        return False
    if (x, i, j) not in mem:
        for sym, rhs in rules:
            for rh in rhs:
            if gen2(x, s, i, j, mem, rule):
                mem[(x, i, j)] = True
                return True
        mem[(x, i, j)] = False
        return False
    else:
        return mem[(x, i, j)]
    
def gen(start, s, rules):
    mem = {}

cnt = 0
for s in strings[1:]:
    syms = parse(s, rules)
    print(len(s))
    for p in sorted(syms.keys(), key = lambda p: (p[1], -p[0])):
        print (p)
    if '0' in syms[(0, len(s))]:
        print ("YES", s)
        cnt += 1
    else:
        print("NO ", s)
    break
# print(lines)a









print("part 1", cnt)


print("part 2", None)

split(9, 3)
