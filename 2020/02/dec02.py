import sys

def parse(line):
    a, b, c = line.split()
    lo, hi = map(int, a.split('-'))
    x = b.strip(':')
    y = c.strip()
    assert len(x) == 1
    return dict(lo=lo, hi=hi, c=x, pw=y)

def valid1(d):
    y = len([1 for x in d['pw'] if x == d['c']])
    return d['lo']<= y <= d['hi']

def valid2(d):
    pw = d['pw']
    lo = d['lo'] - 1
    hi = d['hi'] -1
    if hi >= len(pw):
        return false
    return pw[lo] != pw[hi] and d['c'] in (pw[lo], pw[hi])

items = []
for line in sys.stdin:
    items.append(parse(line))

print(len(list(filter(valid1, items))))
print(len(list(filter(valid2, items))))

