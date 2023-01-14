import sys


def parse(x):
    return x


lines = [parse(x.strip()) for x in sys.stdin]

elves = [0]
for l in lines:
    if l:
        elves[-1] += int(l)
    else:
        elves += [0]









print("part 1", None)
print (max(elves))


print("part 2", None)
print(sum(sorted(elves, reverse=True)[:3]))
