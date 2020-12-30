import sys
import re
from collections import  defaultdict


class Food(object):
    line_pattern = re.compile('([a-z ]+)[(]contains([a-z, ]+)[)]')
    item_pattern = re.compile('[a-z]+')

    def __init__(self, ingredients, alergenes):
        self.ingredients = ingredients
        self.alergenes = alergenes

    @staticmethod
    def parse(line):
        try:
            return Food.parse1(line)
        except:
            print(line)
            raise

    @staticmethod
    def parse1(line):
        m = Food.line_pattern.fullmatch(line.strip())
        assert m
        ings = m.group(1).strip().split()
        for i in ings:
            assert Food.item_pattern.fullmatch(i)
        algs = m.group(2).strip().split(', ')
        for a in algs:
            assert Food.item_pattern.fullmatch(a)
        return Food(set(ings), set(algs))


def read_food(inp):
    return [Food.parse(line) for line in inp]


def solve1(foods):
    algs = {}
    for f in foods:
        for a in f.alergenes:
            if a not in algs:
                algs[a] = f.ingredients
            else:
                algs[a] = algs[a].intersection(f.ingredients)
    change = True
    while change:
        change = False
        for a, ings in algs.items():
            if len(ings) == 1:
                ing = next(iter(ings))
                for a1, ings1 in algs.items():
                    if a1 != a and ing in ings1:
                        change = True
                        algs[a1].remove(ing)
        print()
        for a in algs:
            print(a, algs[a])


    dangerous = set()
    for ings in algs.values():
        dangerous.update(ings)
    print(dangerous)

    cnt = 0
    for f in foods:
        cnt += len(f.ingredients.difference(dangerous))
    print("part 1", cnt)

    items = sorted(algs.items())
    print(items)
    sorted_dangerous = [next(iter(y)) for x, y in items]
    print(sorted_dangerous)
    print(','.join(sorted_dangerous))


def main(inp):
    foods = read_food(inp)
    for food in foods:
        print(len(food.ingredients), len(food.alergenes))
    solve1(foods)


if __name__ == '__main__':
    with open(sys.argv[1]) as inp:
        main(inp)
