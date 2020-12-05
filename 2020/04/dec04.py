import sys

KEYS=set(
    ["byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"])

def parse(data):
    d = {}
    for line in data:
        line = line.strip()
        if not line:
            yield d
            d = {}
            continue
        items = line.strip().split()
        for item in items:
            k, v = item.split(':')
            assert(k)
            assert(k in KEYS)
            assert(v)
            assert(k not in d)
            d[k] = v
    yield d

passports = list(parse(sys.stdin))
print(len(passports))

have_keys = [p for p in passports if set(p.keys()) == KEYS or set(p.keys()) == (KEYS - set(['cid']))]

#1
print(len(have_keys))


#2
import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
YEAR = re.compile("[12][0-9]{3}")


# hgt (Height) - a number followed by either cm or in:
#  If cm, the number must be at least 150 and at most 193.
#  If in, the number must be at least 59 and at most 76.
HGT_CM = re.compile("1[0-9]{2}cm")
HGT_IN = re.compile("[567][0-9]in")

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
HCL = re.compile("#[0-9a-f]{6}")

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
ECL = re.compile("amb|blu|brn|gry|grn|hzl|oth")

# pid (Passport ID) - a nine-digit number, including leading zeroes.
PID = re.compile("[0-9]{9}")


def is_year(s, lo, hi):
    m = YEAR.fullmatch(s)
    if not m:
        return False
    return lo <= int(s) <= hi


def valid_values(p):
    if not is_year(p['byr'], 1920, 2002):
        return False
    if not is_year(p['iyr'], 2010, 2020):
        return False
    if not is_year(p['eyr'], 2020, 2030):
        return False

    hgt = p['hgt']
    m = HGT_CM.fullmatch(hgt)
    if m:
        if not(150 <= int(hgt[0:-2]) <= 193):
            return False
    else:
        m = HGT_IN.fullmatch(hgt)
        if not (m and (59 <= int(hgt[0:-2]) <= 76)):
            return False
    
    if not HCL.fullmatch(p['hcl']):
        return False
    if not ECL.fullmatch(p['ecl']):
        return False
    if not PID.fullmatch(p['pid']):
        return False
    return True

valid = [p for p in have_keys if valid_values(p)]


print(len(valid))


# cnt = 0
# n = 0
# for d in parse(sys.stdin):
#     n += 1
#     x = set(d.keys())
#     x.add('cid')
#     if KEYS == x:
#         cnt += 1

# print(cnt)
# print(n)

