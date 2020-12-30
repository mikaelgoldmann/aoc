import sys
from collections import deque


def read_deck(inp):
    player = inp.readline()
    assert player.startswith("Player")
    d = []
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


def play_game_1(d1, d2):
    dq1 = deque(d1)
    dq2 = deque(d2)
    while dq1 and dq2:
        play(dq1, dq2)
    print(dq1, dq2)
    pts = points(dq1) if d1 else points(dq2)
    return pts


def main(inp):
    d1 = read_deck(inp)
    d2 = read_deck(inp)
    assert len(d1) == len(d2)
    print(d1, d2)
    pts = play_game_1(d1, d2)
    print(d1, d2)
    print("part 1", pts)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)