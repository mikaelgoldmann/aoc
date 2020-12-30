from collections import deque


def rot(d):
    x = d.popleft()
    d.append(x)


def step(d, n):
    def nxt(m):
        m -= 1
        if m < 1:
            return n - 1
        return m

    # current pos is always the first pos!
    elts = []
    current = d.popleft()
    for i in range(3):
        elts.append(d.popleft())
    d.appendleft(current)
    target = nxt(current)
    while target in elts:
        target = nxt(target)
    while d[-1] != target:
        rot(d)
    d.extend(elts)
    while d[-1] != current:
        rot(d)


def main(case, data, steps):
    print()
    print(case, steps)
    data = deque([int(x) for x in data])
    assert set(data) == set(range(1, 10))
    #print("Step", 0)
    #print(data)
    for i in range(steps):
        #print(i)
        step(data, 10)
        #print("Step", i + 1)
        #print(data)
    while data[0] != 1:
        rot(data)
    result = map(str, data)
    print("step 1", ''.join(result)[1:])


if __name__ == '__main__':
    main("test", "389125467", 10)
    main("test", "389125467", 100)
    main("real", "789465123", 100)
