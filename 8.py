from typing import List, Tuple, Set, Callable
from itertools import takewhile, product
from utils import read_input


def main():
    seeable = set()
    for i in range(0, len(forest)):
        see_trees(trees_e(i, -1), seeable)  # ew
        see_trees(trees_w(i, len(forest)), seeable)  # we
    for i in range(0, len(forest[0])):
        see_trees(trees_s(-1, i), seeable)  # ns
        see_trees(trees_n(len(forest), i), seeable)
    print(len(seeable))

    print(max(scenic_score(c) for c in product(range(0, len(forest)), range(0, len(forest[0])))))


def scenic_score(c):
    (y, x) = c
    my_height = forest[y][x][2]
    return look(trees_w(y, x), my_height) *\
        look(trees_n(y, x), my_height) *\
        look(trees_e(y, x), my_height) *\
        look(trees_s(y, x), my_height)


def look(view, until_height):
    next_occluded = False

    def occluded(t):
        nonlocal next_occluded
        me_occluded = next_occluded
        next_occluded = t[2] >= until_height
        return me_occluded

    return len(list(takewhile(lambda t: not occluded(t), view)))


def see_trees(view: List[Tuple[int, int, int]], acc: Set[Tuple[int, int, int]]):
    m = max(enumerate(view), key=lambda e: e[1][2])  # find index of biggest tree
    acc.add(m[1])
    see_trees(new_view, acc) if (new_view := view[0:m[0]]) else acc


def trees_e(y, x):
    return [forest[y][j] for j in range(x + 1, len(forest))]


def trees_w(y, x):
    return [forest[y][j] for j in range(x - 1, -1, -1)]


def trees_n(y, x):
    return [forest[j][x] for j in range(y - 1, -1, -1)]


def trees_s(y, x):
    return [forest[j][x] for j in range(y + 1, len(forest))]


lines = read_input()
forest: List[List[Tuple[int, int, int]]] = [[(i, j, int(lines[i][j])) for j in range(0, len(lines[i]))] for i in
                                            range(0, len(lines))]


if __name__ == "__main__":
    main()
