from collections import deque


def rot(d):
    x = d.popleft()
    d.append(x)


def step(lst, n):
    def nxt(m):
        m -= 1
        if m < 1:
            return n - 1
        return m

    # current pos is always the first pos!
    elts = []
    current = lst.current
    for i in range(3):
        elt = lst.right(current)
        lst.out(elt)
        elts = [elt] + elts  # reverse order for easier insertion
    target = nxt(current)
    while target in elts:
        target = nxt(target)
    for e in elts:  # here it helps that elts are reversed
        lst.insert_after(e, target)
    lst.current = lst.right(current)


class Link(object):
    def __init__(self, me, lft, rte):
        self.me = me
        self.left = lft
        self.right = rte

    def out(self, links):
        lft = links[self.left]
        rte = links[self.right]
        lft.right = self.right
        rte.left = self.left
        self.left = None
        self.right = None

    def insert_after(self, other, links):
        assert self.left is None and self.right is None
        lft = links[other]
        rte = links[lft.right]
        self.left = other
        self.right = lft.right
        lft.right = self.me
        rte.left = self.me


class List(object):
    def __init__(self, current, links):
        self.current = current
        self.links = links

    def out(self, name):
        assert self.current != name
        return self.links[name].out(self.links)

    def insert_after(self, to_insert, after):
        self.links[to_insert].insert_after(after, self.links)

    def left(self, pos):
        return self.links[pos].left

    def right(self, pos):
        return self.links[pos].right


def main(data, steps):
    links = {}
    data = [int(x) for x in data]
    for i in range(len(data)):
        links[data[i]] = Link(data[i], data[i-1], data[(i + 1) % len(data)])

    assert set(data) == set(range(1, 10))
    #print("Step", 0)
    #print(data)
    my_list = List(data[0], links)
    for i in range(steps):
        #print(i)
        step(my_list, 10)
        #print("Step", i + 1)
        #print(data)
    pos = my_list.right(1)
    result = []
    while pos != 1:
        result.append(str(pos))
        pos = my_list.right(pos)
    return ''.join(result)


if __name__ == '__main__':
    for times in [10, 100]:
        print("test step 1:", times, "-" , main("389125467", times))
    print("real step 1:", times, "-", main("789465123", times))
