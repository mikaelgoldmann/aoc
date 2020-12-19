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
   opts = tuple(tuple(int(z) for z in y.strip().split()) for y in rest.split('|'))
   for o in opts:
       if len(o) > 2:
           print (len(o))
   return ('rule', (int(x), opts)) 


lines = [parse_line(x.strip()) for x in sys.stdin]
lines = [line for line in lines if line]

strings = [ y for x,y in lines if x == 'string'  ]
rules =  dict([ y for x,y in lines if x == 'rule'  ])

print(rules)

def gen2(xs, s, i, j, mem, rules):
    if not xs:
        return i == j
    if j <= i:
        return False
    x = xs[0]
    xs = xs[1:]
    for k in range(i + 1, j + 1):
        if gen1(x, s, i, k, mem, rules) and gen2(xs, s, k, j, mem, rules):
            return True
    return False
        
        

def gen1(x, s, i, j, mem, rules):
    if j <= i:
        return False
    if i + 1 == j and x == s[i]:
        return True
    if (x, i, j) not in mem:
        for sym, rhs in rules.items():
            if sym != x:
                continue
            for rh in rhs:
                if gen2(rh, s, i, j, mem, rules):
                    mem[(x, i, j)] = True
                    return True
        mem[(x, i, j)] = False
        return False
    else:
        return mem[(x, i, j)]
    
def gen(start, s, rules):
    mem = {}
    tt = gen1(start, s, 0, len(s), mem, rules)
#    print(mem)
    return tt


cnt = 0
for s in strings:
    if gen(0, s, rules):
        print ("YES", s)
        cnt += 1
    else:
        print("NO ", s)
# print(lines)a









print("part 1", cnt)


print("part 2", None)

