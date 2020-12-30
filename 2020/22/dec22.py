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


def points(d1, d2=None):
    assert not d1 or not d2
    d = deque(d1 or d2)
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
    return dq1, dq2


def round(dq1, dq2):
    c1 = dq1.popleft()
    c2 = dq2.popleft()
    if c1 > len(dq1) or c2 > len(dq2):
        # highest card wins
        if c1 > c2:
            dq1.extend([c1, c2])
        else:
            dq2.extend([c2, c1])
    else:
        # play recursive game
        s1, s2 = play_game_2(list(dq1)[:c1], list(dq2)[:c2])
        if s1:
            dq1.extend([c1, c2])
        else:
            dq2.extend([c2, c1])


def play_game_2(d1, d2):
    # returns dq1 , dq2 which are the winners deque and the losers (empty) deque
    dq1 = deque(d1)
    dq2 = deque(d2)
    seen = set()
    while dq1 and dq2:
        key = (tuple(dq1), tuple(dq2))
        if key in seen:
            return list(dq1), []
        round(dq1, dq2)
        seen.add(key)
    return dq1, dq2


def main(inp):
    d1 = read_deck(inp)
    d2 = read_deck(inp)
    assert len(d1) == len(d2)
    # print(d1, d2)
    pts = points(*play_game_1(d1, d2))
    # print(d1, d2)
    print("part 1", pts)
    s1, s2 = play_game_2(d1, d2)
    pts = points(s1, s2)
    print("part 2", pts)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)