import sys



ns = [int(x.strip()) for x in sys.stdin]



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
s = ns[0] + ns[1]
while s != c:
    if j < k - 1 and s > c:
        s -= ns[j]
        j += 1
    else:
        k += 1
        s += ns[k]

y = ns[j: k + 1]
print("part 2")
print(c, sum(y))
print(j, k+1)
print(min(y), max(y))
print("sol", min(y) +max(y))

