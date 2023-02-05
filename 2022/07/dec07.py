import sys
from collections import deque


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


def parse_line(line: str):
    if line.startswith('$ cd '):
        return ('cd', line.split()[2].strip())
    if line.startswith('$ ls'):
        return ('ls',)
    if line.startswith('dir '):
        return ('dir', line.split()[1].strip())
    sz, name = line.strip().split()
    return ('file', name, int(sz))


class Node(object):
    def __init__(self, kind, name, parent, size):
        self.kind = kind
        self.name = name
        self.parent = parent
        self. size = size
        self.nodes = {'..': parent}

    @staticmethod
    def mk_dir(name, parent):
        return Node('dir', name, parent, 0)

    @staticmethod
    def mk_file(name, parent, size):
        return Node('file', name, parent, size)


def build_tree(node: Node, dq:deque):
    while True:
        if len(dq) == 0:
            return
        x = dq.popleft()
        if x[0] == 'cd':
            build_tree(node.nodes[x[1]], dq)
            return
        if x[0] == 'ls':
            nodes = ls(node, dq)
            for n in nodes:
                node.nodes[n.name] = n


def ls(parent: Node, dq: deque):
    nodes = []
    while True:
        if len(dq) == 0:
            return nodes
        x = dq.popleft()
        if x[0] == 'dir':
            nodes.append(Node.mk_dir(x[1], parent))
        elif x[0] == 'file':
            nodes.append(Node.mk_file(x[1], parent, x[2]))
        else:
            dq.appendleft(x)
            return nodes


def make_tree(dq: deque):
    d = dq.popleft()
    assert d == ('cd', '/')
    root = Node.mk_dir('/', None)
    build_tree(root, dq)
    return root


def sum_tree(node: Node):
    if node.kind == 'file':
        return node.size
    s = 0
    for name, n in node.nodes.items():
        if name != '..':
            s += sum_tree(n)
    node.size = s
    return s


def print_tree(node: Node, indent=''):
    print(indent, node.kind, node.name, node.size)
    for name, n in node.nodes.items():
        if name != '..':
            print_tree(n, indent + '    ')


def all_dirs(node: Node, dirs=[]):
    if None or node.kind == 'file':
        return dirs
    dirs.append(node)
    for name, n in node.nodes.items():
        if name != '..':
            all_dirs(n, dirs)
    return dirs


if __name__ == '__main__':
    lines = get_lines()

    dq = deque(map(parse_line, lines))
    tree = make_tree(dq)
    sum_tree(tree)
    print("part 1", None)
    # print_tree(tree)
    dirs = all_dirs(tree)
    print(sum(map(lambda n: n.size, filter(lambda n: n.size <= 100000, dirs))))

    print("part 2", None)
    to_delete = 30000000 - (70000000 - tree.size)
    print(min(map(lambda n: n.size, filter(lambda n: n.size >= to_delete, dirs))))

