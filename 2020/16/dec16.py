import sys


data = sys.stdin.read()

rules, my_ticket, other_tickets = data.strip().split('\n\n')

# print('*')
# print(rules)
# print('*')
# print(my_ticket)
# print('*')
# print(other_tickets)
# print('*')


def parse_interval(v):
    lo, hi = v.split('-')
    return int(lo), int(hi)


def parse_rule(rule):
    t, rest = rule.split(':')
    fst, lst = rest.strip().split(' or ')
    return t, parse_interval(fst), parse_interval(lst)


def parse_rules(rules):
    d = {}
    for r in rules.split('\n'):
        (t, fst, lst) = parse_rule(r)
        d[t] = (fst, lst)
    return d


def parse_ticket(t):
    return [int(x) for x in t.split(',')]
    

def parse_tickets(o):
    lines = o.split('\n')
    return [parse_ticket(x) for x in lines[1:]]


def matching_rules(value, rules):
    m = []
    for (t, v) in rules.items():
        ((l1, h1), (l2, h2)) = v
        if (l1 <= value <= h1) or (l2 <= value <= h2):
            m.append(t)
    return m


def simple_check(ticket, rules):
    unmatched = []
    for v in ticket:
        if not matching_rules(v, rules):
            unmatched.append(v)
    return unmatched
    

rules = parse_rules(rules)
other_tickets = parse_tickets(other_tickets)
[my_ticket] = parse_tickets(my_ticket)

tot = 0
valid_tickets = []
for ticket in other_tickets:
    unmatched = simple_check(ticket, rules)
    is_valid = len(unmatched) == 0
    tot += sum(unmatched)
    if is_valid:
        valid_tickets.append(ticket)

print("part 1", tot)


possible = dict((pos, set(rules.keys())) for pos in range(len(my_ticket)))

for ticket in valid_tickets:
    for pos in range(len(my_ticket)):
        a = possible[pos]
        b = matching_rules(ticket[pos], rules)
        possible[pos] = a.intersection(b)


# check for simplifying structure
s = set()
for k,v in sorted(possible.items(), key = lambda p: len(p[1])):
    print (k, len(v))
    assert set(v).union(s) == set(v)
    s = set(v)

# This abuses the fact that the posibilities in the test data have a very simple structure.
used = set()
sol = {}
for k,v in sorted(possible.items(), key = lambda p: len(p[1])):
    vset = set(v)
    assert used.difference(vset) == set()
    s = set(v).difference(used)
    assert len(s) == 1
    sol[s.pop()] = k
    used = vset

print(sol)

s = 1
for name, val in sol.items():
    if name.startswith('departure'):
        s *= my_ticket[val]

print("part 2", s)







