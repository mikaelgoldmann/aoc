import sys
from collections import deque


def read_deck(inp):
    player = inp.readline()
    assert player.startswith("Player")
    d = deque()
    for line in inp:
        if not line.strip():
            return d
        d.append(int(line.strip()))
    return d


def play(d1, d2):
    c1 = d1.popleft()
    c2 = d2.popleft()
    assert c1 != c2
    if c1 > c2:
        d1.append(c1)
        d1.append(c2)
    else:
        d2.append(c2)
        d2.append(c1)


def points(d):
    mult = 1
    sum = 0
    while d:
        c = d.pop()
        sum += mult * c
        mult += 1
    return sum


def main(inp):
    d1 = read_deck(inp)
    d2 = read_deck(inp)
    assert len(d1) == len(d2)
    print(d1, d2)
    while d1 and d2:
        play(d1, d2)
    print(d1, d2)
    print("part 1", points(d1) if d1 else points(d2))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)