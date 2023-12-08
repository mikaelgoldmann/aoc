import sys
from collections import namedtuple


Game = namedtuple('Game', ('game_num', 'card', 'nums'))


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
        int_lines.append(get_int_line(line))
    return int_lines


def get_int_line(line: str) -> list:
    int_line = []
    for x in line.split():
        try:
            x = int(x)
            int_line.append(x)
        except:
            pass
    return int_line


def matches(game: Game) -> int:
    card = set(game.card)
    nums = set(game.nums)
    return len(card.intersection(nums))


def score(game: Game) -> int:
    m = matches(game)
    if m == 0:
        return 0
    return 2 ** (m - 1)


class Card(object):
    def __init__(self, card_number, card, numbers):
        this

def main(argv):
    lines = get_lines()

    pts = 0
    games = {}
    count = {}
    for line in lines:
        head, tail = line.split(':')
        game_number, = get_int_line(head)
        card, numbers = tail.split('|')
        games[game_number] = Game(game_number, get_int_line(card), get_int_line(numbers))
        count[game_number] = 1

    print("part 1")
    for i, game in games.items():
        assert i == game.game_num
        pts += score(game)
    print(pts)

    print("part 2")
    s = 0
    for game_num in sorted(count.keys()):
        # print(game_num, matches(games[game_num]))
        for i in range(matches(games[game_num])):
            if (game_num + i + 1) in count:
                count[game_num + i + 1] += count[game_num]
        s += count[game_num]
        # print(game_num, count[game_num])
    print(s)

if __name__ == '__main__':
    main(sys.argv)
