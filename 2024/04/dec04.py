import sys
from http.cookiejar import debug

SAM = "SAM"

MAS = "MAS"

XMAS = 'XMAS'


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


def xmas(board, r, c,  dr, dc, s):
    if s == "":
        return True
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
        return False
    if board[r][c] != s[0]:
        return False
    return xmas(board, r + dr, c + dc, dr, dc, s[1:])


def solve1(board):
    debug = [['.'] * len(board[0]) for x in board]
    s = 0
    for dr in range(-1,2):
        for dc in range(-1,2):
            if dr == 0 and dc == 0:
                continue
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if xmas(board, r, c, dr, dc, XMAS):
                        # print(">>>>", r, c, dr, dc)
                        for i in range(len(XMAS)):
                            debug[r + i * dr][c + i * dc] = XMAS[i]
                            # print("(%d,%d) " % (r + i * dr, c + i * dc), )
                       # print()
                        s += 1
    #for d in debug:
    #    print(''.join(d))
    return s


def mas(board, r, c, dr, dc, s):
    for i in range(len(s)):
        if board[r + i * dr][c + i * dc] != s[i]:
            return False
    return True


def solve2(board):
    s = 0
    for r in range(len(board) - 2):
        for c in range(len(board[r]) - 2):
            if ((mas(board, r, c, 1, 1, MAS) or mas(board, r, c, 1, 1, SAM)) and
            (mas(board, r, c + 2, 1, -1, MAS) or mas(board, r, c + 2, 1, -1, SAM))):
                s += 1
    return s


def main(argv):
    board = get_lines()
    print("part 1")
    print(solve1(board))
    print()
    print("part 2")
    print(solve2(board))


if __name__ == '__main__':
    main(sys.argv)
