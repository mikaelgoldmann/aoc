import sys


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


def fill(board: list, nums: list, i:int , j: int):
    print("fill", i, j)
    for di in range(-1, 2):
        for dj in range(-1, 2):
            try:
                c = board[i + di][j + dj]
                if c.isdigit():
                    k = j + dj
                    while k >= 0 and board[i + di][k].isdigit():
                        nums[i + di][k] = True
                        k -= 1
                    k = j + dj
                    while k < len(board[0]) and board[i + di][k].isdigit():
                        nums[i + di][k] = True
                        k += 1
            except IndexError:
                pass


def get_numbers(brow, nrow):
    r = []
    v = 0
    for b, n in zip(brow, nrow):
        if n:
            v = v * 10 + ord(b) - ord('0')
        else:
            if v:
                r.append(v)
            v = 0
    if v:
        r.append(v)
        print(r)
    return r


def main(argv):
    board = get_lines()

    print("part 1")
    nums = [[False for j in range(len(board[0]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.' and not board[i][j].isdigit():
                fill(board, nums, i, j)

    s = 0
    for brow, nrow in zip(board, nums):
        s += sum(get_numbers(brow, nrow))

    print(s)
    print("part 2")


if __name__ == '__main__':
    main(sys.argv)
