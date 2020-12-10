import sys

adapters = sorted(int(x.strip()) for x in sys.stdin)

print(adapters)

d = []
x = 0

for y in adapters:
    d.append(y - x)
    x = y

d.append(3)  # diff to device joltage
 
ones = len([d1 for d1 in d if d1 == 1])
threes = len([d1 for d1 in d if d1 == 3])

print(d)
print(ones, threes)

print("part 1", ones * threes)


# c[i] == number of ways to get to voltage i
c = [0] * (max(adapters) + 1)
c[0] = 1

for a in adapters:
    c[a] = c[a - 1] + c[a - 2] + c[a - 3]

print("part 2", c[adapters[-1]])

    
