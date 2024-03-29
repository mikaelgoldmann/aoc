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


if __name__ == '__main__':

    txt = sys.stdin.readline().strip()

    print("part 1", None)
    for i in range(4, len(txt)):
        if len(set(txt[i-4:i])) == 4:
            print(i)
            break

    print("part 2", None)
    for i in range(14, len(txt)):
        if len(set(txt[i-14:i])) == 14:
            print(i)
            break
