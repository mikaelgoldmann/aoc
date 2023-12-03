import sys


NUMERALS = 'one, two, three, four, five, six, seven, eight, nine'.split(', ')

for N in NUMERALS:
    print('<' + N + '>')

def get_lines(f=None):
    if not f:
        f = sys.stdin
    return [x.strip() for x in f]


def get_paragraphs(lines=None):
    if lines is None:
        lines = get_lines()
    paragraph = []
    for x in lines:
        x = x.strip()
        if not x:
            yield paragraph
            paragraph = []
        else:
            paragraph.append(x)
    if paragraph:
        yield paragraph


def get_int_lines(lines=None):
    if lines is None:
        lines = get_lines()
    int_lines = []
    for line in lines:
        int_line = []
        for x in line.split():
            try:
                x = int(x)
                int_line.append(x)
            except:
                pass
        int_lines.append(int_line)
    return int_lines


def compute(lines, use_numerals=False):
    s = 0
    for line in lines:
        digs = get_digits(line, use_numerals)
        s += (digs[0]*10 + digs[-1])
    return s


def get_digits(line, use_numerals=False):
    global NUMERALS
    digs = []
    i = 0
    while i < len(line):
        # print(line[i:])
        if line[i].isdecimal():
            digs.append(int(line[i]))
        elif use_numerals:
            for (n, numeral) in enumerate(NUMERALS):
                # print(numeral)
                if line[i:].startswith(numeral):
                    digs.append(n+1)
        i += 1
    #print(digs)
    return digs


if __name__ == '__main__':

    lines = get_lines()
    print("part 1")
    try:
        print(compute(lines))
    except:
        print("part 1 error for input")

    print()
    print("part 2")
    try:
        print(compute(lines, use_numerals=True))
    except:
        print("part 2 error for input")
