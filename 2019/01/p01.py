import sys


lines = [x.strip() for x in sys.stdin]

tot = 0

def f(x):
    return (x // 3) - 2

def f2(x):
    s = f(x)
    e = s
    while f(e) > 0:
        s += f(e)
        e = f(e)
    return s

for x in lines:
    tot += f(int(x))
    

print("part 1", tot)

tot = 0
for x in lines:
    tot += f2(int(x))

print("too big", 5022603)
print("part 2", tot)

