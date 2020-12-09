import sys



ns = [int(x.strip()) for x in sys.stdin]


# sanity check

pre = int(sys.argv[1]) if len(sys.argv) == 2 else 25

print(pre)

def check(i):
    for j in range(i - pre, i):
        for k in range(j + 1, i):
            if ns[j] + ns[k] == ns[i]:
                print(ns[j], '+', ns[k], '=', ns[i])
                return -1
    return ns[i]


for i in range(pre, len(ns)):
    c = check(i)
    if c != -1:
        print(c)
        break

sums = []
s = 0
for i in range(len(ns)):
    s += ns[i]
    sums.append(s)

j = 0
k = 1
s = sums[1]
while s != c:
    if j < k - 1 and  

