import sys
import egcd


def parse(x):
    return x


lines = [x.strip() for x in sys.stdin]

T = int(lines[0])
IDs = [int(x) for x in lines[1].split(',') if x != 'x']


def r(t, id):
    rem = t % id
    if rem == 0:
        return 0
    else:
        return id - rem


id = IDs[0]
rem = r(T, id)

for i in IDs:
    if r(T, i) < rem:
        rem = r(T, i)
        id = i

print(id, rem)

print("part 1", id * rem)

# for i in range(len(IDs)):
#     for j in range(i+1, len(IDs)):
#         # check rel prime
#         assert egcd.egcd(IDs[i], IDs[j])[0] == 1

# print ("input ok")

def lcm(a, b):
    return (a * b) // egcd.egcd(a, b)[0]

def parse2(ids):
    ids = ids.split(',')
    for i in range(len(ids)):
        if ids[i] != 'x':
            yield (i, int(ids[i]))

x = list(parse2(lines[1]))

print(x)

m = 1
t = 0

for rem, id in x:
    print()
    # there should be a departure of bus id at rem minutes after t
    # so k * id = t +rem has an integer solution k
    # so id divides (t + rem)
    while (t + rem) % id != 0:        
        t += m
    print((rem, id), t, m)
    m = lcm(m, id)

for rem, id in x:
    print(id, rem, r(t, id))

print("part 2", t)
