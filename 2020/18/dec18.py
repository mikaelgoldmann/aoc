import sys


def tokens(w):
    if w in "+*":
        return [w]

    t = []
    while w.startswith('('):
        t.append('(')
        w = w[1:]
    rest = []
    while w.endswith(')'):
        rest.append(')')
        w = w[:-1]
    return t + [int(w)] + rest


def lex(line):
    toks = []
    words = line.split()
    for w in words:
        toks.extend(tokens(w))
    return toks


lines = [lex(x.strip()) for x in sys.stdin]


def term(toks, pos, expr_):
    if toks[pos] == '(':
        val, pos = expr_(toks, pos + 1)
        assert toks[pos] == ')'
        return val, pos + 1
    else:
        return toks[pos], pos + 1

def expr_(toks, pos):
    acc, pos = term(toks, pos, expr_)
    while pos < len(toks) and toks[pos] != ')':
        op = toks[pos]
        n, pos = term(toks, pos + 1, expr_)
        if op == '+':
            acc += n
        elif op == '*':
            acc *= n
        else:
            assert False
    return acc, pos


tot = 0
for toks in lines:
    val, pos = expr_(toks, 0)
    assert pos == len(toks)
    print(val)
    tot += val


print("part 1", tot)


def sum_(toks, pos):
    pos1 = pos
    acc, pos = term(toks, pos, prod_)
    while pos < len(toks) and toks[pos] == '+':
        n, pos = term(toks, pos + 1, prod_)
        acc += n
    return acc, pos

def prod_(toks, pos):
    acc, pos = sum_(toks, pos)
    while pos < len(toks) and toks[pos] == '*':
        s, pos = sum_(toks, pos + 1)
        acc *= s
    return acc, pos

tot = 0
for toks in lines:
    val, pos = prod_(toks, 0)
    assert pos == len(toks)
    print(val)
    tot += val

print("part 2", tot)
