from lib19 import intcode as ic
import sys


def get_state(out):
    board = {}
    pts = 0
    paddle = 0, 0
    ball = 0, 0
    for i in range(0, len(out), 3):
        x, y, v = out[i:i+3]
        if x == -1 and y == 0:
            pts = v
        else:
            if v == 3:
                paddle = x, y
            elif v == 4:
                ball = x, y
            board[(x, y)] = v
    return board, pts, paddle, ball


def print_state(out):
    state, pts, paddle, ball = get_state(out)
    print("points", pts)
    print("ball", ball)
    print("paddle", paddle)
    minx = min(x for x, _ in state)
    maxx = max(x for x, _ in state)
    miny = min(y for _, y in state)
    maxy = max(y for _, y in state)
    assert (minx, miny) == (0, 0)  # just checking assumptions
    for y in range(maxy + 1):
        print(''.join([str(state.get((x, y), 0)) for x in range(maxx + 1)]))
    print()


def solve1(prog):
    r = ic.run(prog, iter([]))
    out = []
    running = True
    while running:
        mem, o, pc, running = next(r)
        if o is not None:
            out.append(o)
    blocks = set()
    for i in range(0, len(out), 3):
        x, y, kind = out[i:i+3]
        if kind == 2:
            blocks.add((x,y))
    print("part 1", len(blocks))
    print_state(out)


class Moves(object):
    def __init__(self, moves):
        self._moves = moves
        self._cnt = 0
    def __iter__(self):
        for m in self._moves:
            self._cnt += 1
            yield m
        while True:
            self._cnt += 1
            yield 0
    def cnt(self):
        return self._cnt
    def moves(self):
        return self._moves


def get_ball_path(out):
    ball = []
    for i in range(0, len(out), 3):
        x, y, v = out[i:i+3]
        if x == -1 and y == 0:
            continue
        elif v == 4:
            ball.append((x, y))
    return ball


def get_paddle_path(out):
    paddle = []
    for i in range(0, len(out), 3):
        x, y, v = out[i:i+3]
        if x == -1 and y == 0:
            continue
        elif v == 3:
            paddle.append((x, y))
    return paddle


#
# Run until first input is required. Save the state s0 = (intcode computer mem and pc)
# go stepwise with input = 0 until ball is at x0, y == 23 at time t0
# Restart computer from s0 and use inputs that get paddle to x0, 24 by time t0.
# Remember inputs used. Then start from s0 again finding second time ball gets to x1, y == 23
# at time t1 and extend inputs so that between t0 and t1 the paddle moves to x1, 24.
# Repeat until one of the following happen:
# * program halts for some reason
# * No more blocks (?)

def get_moves(ball_path, paddle_start):
    px, py = paddle_start
    targets = []
    moves = []
    for i, (x, y) in enumerate(ball_path):
        if y == py - 1:
            targets.append((i, x))
    print(targets)
    step = 0
    for i, x in targets:
        while step <= i and px < x:
            moves.append(1)
            step += 1
            px += 1
        while step <= i and px > x:
            moves.append(-1)
            step += 1
            px -= 1
        while step <= i:
            moves.append(0)
            step += 1
    print(moves)
    return moves



def solve2(prog):
    moves = []
    for k in range(800):
        inp = Moves(moves)
        out = run_until_stop(inp, prog[:])
        print_state(out)
        ball_path = get_ball_path(out)
        print(ball_path)
        paddle_path = get_paddle_path(out)
        print(paddle_path)
        moves = get_moves(ball_path, paddle_path[0])
        print(inp.cnt())
        board, pts, paddle, ball = get_state(out)
        nblocks = len(list(filter(lambda x: x == 2, board.values())))
        print(nblocks)
        if not nblocks:
            break
    print("points", pts)


def run_until_stop(inp, prog):
    r = ic.run(prog, iter(inp))
    out = []
    running = True
    while running:
        mem, o, pc, running = next(r)
        if o is not None:
            out.append(o)
    #        if ic.parse_op(mem[pc])[0] == ic.OpCode.INP:
    #            print(steps)
    #            steps += 1
    #            print_state(out)
    # inp.append(-1)
    return out


if __name__ == '__main__':
    with open('13.in') as f:
        prog = next(ic.read_prog(f))
    #solve1(prog[:])
    prog[0] = 2
    solve2(prog)