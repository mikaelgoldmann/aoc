import sys


BLOCKS = {'red': 12, 'green': 13, 'blue': 14}


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


def get_set(set_str: str):
    a_set = {}
    for item in set_str.strip().split(','):
        item = item.strip()
        cnt, color = item.split()
        a_set[color.strip()] = int(cnt)
    return a_set


def get_game(line: str):
    assert line.startswith('Game')
    g, sets = line.split(':')
    gnum = g.strip().split()[-1]
    sets = [get_set(s.strip()) for s in sets.split(';')]
    return int(gnum), sets


def valid(a_set):
    for col in a_set:
        if col not in BLOCKS:
            raise Exception
        elif a_set[col] > BLOCKS[col]:
            return False
    return True


def valid_game(sets):
    return all(valid(s) for s in sets)


def min_blocks_power(game):
    mb = dict((c, 0) for c in BLOCKS)
    for g in game:
        for c in g:
            mb[c] = max(mb[c], g[c])
    p = 1
    for val in mb.values():
        p *= val
    return p


if __name__ == '__main__':

    lines = get_lines()
    games = dict(get_game(line) for line in lines)
    print("part 1")
    print(sum(g for g in games if valid_game(games[g])))

    print()
    print("part 2")
    s = 0
    for g in games:
        s += min_blocks_power(games[g])
    print(s)
