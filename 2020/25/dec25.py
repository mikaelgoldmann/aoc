import math


DENOMINATOR = 20201227
SUBJECT_NUMBER = 7

################
# from https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print(a, m)
        raise Exception('modular inverse does not exist')
    else:
        return x % m
###############


def transform(subject_number, value=1, lz=1):
    for i in range(lz):
        value = (value * subject_number) % DENOMINATOR
    return value


def mod_div(a, b, p):
    return (a * modinv(b, p)) % p

def shank(a, b, p):
    # solve a^x == b mod p
    c = int(math.sqrt(DENOMINATOR))
    d = mod_exp(a, c, p)
    prod = 1
    exp = 0
    tab = {}
    while exp < p:
        tab[prod] = exp
        prod *= d
        prod %= p
        exp += c
    prod = 1
    exp = 0
    while mod_div(b, prod, p) not in tab:
        prod *= a
        prod %= p
        exp += 1
    assert mod_exp(a, exp + tab[mod_div(b, prod, p)], p) == b
    return exp + tab[mod_div(b, prod, p)]


def loop_size(pk):
    return shank(SUBJECT_NUMBER, pk, DENOMINATOR)


def mod_exp(a, b, p):
    r = 1
    q = a
    while b:
        if b % 2:
            r = (r * q) % p
        q = (q * q) % p
        b //= 2
    return r


def solve1(card_pk, door_pk):
    lzc = loop_size(card_pk)
    lzd = loop_size(door_pk)
    print(lzc, lzd)
    key1 = mod_exp(card_pk, lzd, DENOMINATOR)
    key2 = mod_exp(door_pk, lzc, DENOMINATOR)
    assert key1 == key2
    return key1


if __name__ == '__main__':
    print("test 1", solve1(5764801, 17807724))
    card_pk = 3469259
    door_pk = 13170438
    print("step 1", solve1(card_pk, door_pk))
