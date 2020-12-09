import sys
from collections import defaultdict, deque
import re


PART = re.compile("([0-9]+) ([a-z]+ [a-z]+) bag[s]{0,1}")

V = set()

CONTAINS = defaultdict(lambda: list())
PARENTS = defaultdict(lambda: list())


def parse_part(parent, part):
    part = part.strip()
    if part == "no other bags":
        return
    m = PART.fullmatch(part)
    assert m
    cnt = int(m.group(1))
    color = m.group(2)
    V.add(color)
    PARENTS[color].append(parent)
    CONTAINS[parent].append((cnt, color))


def parse(line):
    line = line.strip()
    line = line.rstrip('.')
    parts = line.split(',')
    p, x = parts[0].split(' bags contain ')
    p = p.strip()
    V.add(p)
    for part in ([x] + parts[1:]):
        parse_part(p, part)


for line in sys.stdin:
    parse(line)


bag = 'shiny gold'

seen = set()

q = deque()
q.append(bag)


while q:
    h = q.popleft()
    for x in PARENTS[h]:
        if x not in seen:
            seen.add(x)
            q.append(x)

print("part 1:", len(seen))


seen = set([bag])
sys.setrecursionlimit(1000000)


def count_bags(b):
    s = 0
    for cnt, color in CONTAINS[b]:
        s += cnt * (1 + count_bags(color))  # bag itself + bags inside
    return s
    

#print(CONTAINS)
print("part 2:", count_bags(bag))
