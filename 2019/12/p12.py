import sys
import re

RE = re.compile('<x[ ]*=[ ]*([-]*[0-9]+),[ ]*y[ ]*=[ ]*([-]*[0-9]+),[ ]*z[ ]*=[ ]*([-]*[0-9]+)>')


class Moon(object):
    def __init__(self, pos):
        self.pos = pos
        self.v = 0, 0, 0

    def update_v(self, delta):
        self.v = self.add(self.v, delta)

    def step(self):
        self.pos = self.add(self.pos, self.v)

    @staticmethod
    def add(a, b):
        assert len(a) == len(b) == 3
        return tuple(x + y for x, y in zip(a, b))

    def energy(self):
        return self._energy(self.pos) * self._energy(self.v)

    @staticmethod
    def parse(txt):
        m = RE.fullmatch(txt.strip())
        assert m
        pos = tuple(int(m.group(i)) for i in [1, 2, 3])
        return Moon(pos)

    @staticmethod
    def _energy(vals):
        s = 0
        for v in vals:
            s += abs(v)
        return s


def read_moons(inp):
    return [Moon.parse(inp.readline()) for i in range(4)]


def calc_delta(m, moons, i):
    vals = [m1.pos[i] for m1 in moons]
    less = [v for v in vals if v < m.pos[i]]
    more = [v for v in vals if v > m.pos[i]]
    return len(more) - len(less)


def step(moons, n):
    for m in moons:
        delta = tuple(calc_delta(m, moons, i) for i in range(3))
        m.update_v(delta)
    s = 0
    for m in moons:
        m.step()
        s += m.energy()


def main(inp, n):
    # solve step 1
    moons = read_moons(inp)
    for i in range(n):
        step(moons, i + 1)
    s = 0
    for m in moons:
        print(m.pos, m.v)
        s += m.energy()
    print("Total energy", s)


def rho_step(pv):
    p, v = pv
    delta = [0] * len(v)
    for i in range(len(p)):
        for j in range(len(p)):
            if p[j] < p[i]:
                delta[i] -= 1
            elif p[j] > p[i]:
                delta[i] += 1
    v1 = tuple(x + y for x, y in zip(v, delta))
    p1 = tuple(x + y for x, y in zip(p, v1))
    return p1, v1


def rho(moons, i):
    # only used to get an idea of cycle lengths
    p1 = tuple(m.pos[i] for m in moons)
    p2 = p1
    v1 = (0,) * len(moons)
    v2 = v1
    t = 0
    while True:
        t += 1
        p1, v1 = rho_step((p1, v1))
        p2, v2 = rho_step(rho_step((p2, v2)))
        if (p1, v1) == (p2, v2):
            return t


def collide(moons, i):
    # find smallest t0, t1 s/t t0 < t1 and state for
    # coordinate i (position and speed) are the same after
    # t0 and t1 steps (so at time t1 is the first time we
    # return to a previous state for that coordinate.
    #
    # NOTE: For the test input it turns out that t0 = 0 for
    # all 3 coordinates.
    p1 = tuple(m.pos[i] for m in moons)
    v1 = (0,) * len(moons)
    t = 0
    seen = {}
    while (p1, v1) not in seen:
        seen[(p1, v1)] = t
        t += 1
        p1, v1 = rho_step((p1,v1))
    return (p1, v1), seen[(p1, v1)], t


def gcd(a, b):
    if a < 0:
        return gcd(-a, b)
    if b < 0:
        return gcd(a, -b)
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main2(inp):
    # solve second step
    moons = read_moons(inp)
    steps = 1
    for i in range(3):
        state, t0, t1 = collide(moons, i)
        assert t0 == 0  # this is required for solution below to work!
        steps = lcm(t1, steps)
    print("steps", steps)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        # main(f, 1000)
        main2(f)
