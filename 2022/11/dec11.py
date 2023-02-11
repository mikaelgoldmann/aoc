import sys
import re


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


def tst(n):
    return lambda m: (m // 3, m % n)


def op(old, operation, operand):
    v = old if operand == 'old' else int(operand)
    assert operation in ['*', '+']
    return old + v if operation == '+' else old * v


def cond(rem, t, f):
    return t if rem == 0 else f


class Monkey(object):
    def __init__(self, id, items, operation, operand, test, true, false):
        self.id = id
        self.items = items
        self.operation = operation
        self.operand = operand
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0
        self.relief = 3
        self.prod = 1

    def accept(self, item):
        self.items.append(item)

    def turn(self, monkeys):
        items = self.items
        self.items = []
        for item in items:
            self.inspections += 1
            item = op(item,  self.operation, self.operand)
            item = (item // self.relief) % self.prod
            rem = item % self.test
            i = cond(rem, self.true, self.false)
            monkeys[i].accept(item)

    def __str__(self):
        x = ', '.join(map(str, self.items))
        return 'M(%d: items=%s, operation=%s, operand=%s, test=%d, t=%s, f=%s, inspections=%d)' % \
               (self.id, x, self.operation, self.operand, self.test, self.true, self.false, self.inspections)


def one_round(monkeys):
    for m in monkeys:
        m.turn(monkeys)


def get_monkey(lines):
    # Monkey 0:
    #   Starting items: 79, 98
    #   Operation: new = old * 19
    #   Test: divisible by 23
    #     If true: throw to monkey 2
    #     If false: throw to monkey 3
    for l in lines:
        print(l)
    print()
    print(re.match('Monkey ([0-9]+):', lines[0]).group(1))
    id = int(re.match('Monkey ([0-9]+):', lines[0]).group(1))
    its = re.match('Starting items: (.*)', lines[1]).group(1)
    items = [int(x.strip()) for x in its.split(',')]
    print(lines[2])
    m = re.match('Operation: new = old (.) ([^ ]+)$', lines[2])
    operation, operand = m.group(1), m.group(2)
    test = int(re.match('Test: divisible by ([0-9]+)', lines[3]).group(1))
    t = int(re.match('.* ([0-9]+)$', lines[4]).group(1))
    f = int(re.match('.* ([0-9]+)$', lines[5]).group(1))
    return Monkey(id, items, operation, operand, test, t, f)


def out(ms):
    for m in ms:
        print(m)

if __name__ == '__main__':
    ps = [x for x in get_paragraphs()]
    ms = [get_monkey(p) for p in ps]
    product = 1
    for m in ms:
        product *= m.test
    for m in ms:
        m.prod = product
    out(ms)
    print()
    for i in range(20):
        one_round(ms)
    out(ms)
    foo = [(m.inspections) for m in ms]
    a,b = sorted(foo)[-2:]
    print("part 1")
    print (a * b)


    print()
    print("part 2")
    ms = [get_monkey(p) for p in ps]
    product = 1
    for m in ms:
        product *= m.test
    for m in ms:
        m.prod = product
        m.relief = 1
    for i in range(10000):
        one_round(ms)
        out(ms)
    foo = [(m.inspections) for m in ms]
    a,b = sorted(foo)[-2:]
    print(a * b)
