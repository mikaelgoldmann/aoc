lo = 137683
hi = 596253


def valid(n):
    prev = chr(ord('0') - 1)
    dups = False
    for c in str(n):
        if c < prev:
            return False
        if c == prev:
            dups = True
        prev = c
    return dups

assert valid(111111)
assert not valid(223450)
assert not valid(123789)

cnt = 0
for n in range(lo, hi + 1):
    if valid(n):
        cnt += 1


print("part 1", cnt)


def valid2(n):
    small = chr(ord('0') - 1)
    prev = small
    for c in str(n):
        if c < prev:
            return False
        prev = c
    xc = small + str(n) + 'a'
    for i in range(2, len(xc) - 1):
        if xc[i] == xc[i - 1] and xc[i] != xc[i - 2] and xc[i] != xc[i + 1]:
            return True
    return False

assert valid2(112233)
assert not valid2(123444)
assert valid2(111144)

cnt = 0
for n in range(lo, hi + 1):
    if valid2(n):
        cnt += 1


print("part 2", cnt)
            
        
    
