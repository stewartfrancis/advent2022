import re

from utils import read_input
from more_itertools import split_at


def main():
    lines = read_input()
    stacks, instructions = split_at(lines, lambda x: x == '')
    stacks = stacks[:-1]
    keep_indices = list(map(lambda x: (x * 4) + 1, range(9)))
    stacks = [line.ljust(35) for line in stacks]
    stacks = [[line[index] for index in keep_indices] for line in stacks]
    stacks = [enumerate(line, 1) for line in stacks]
    stacks = [list(filter(lambda x: x[1] != ' ', line)) for line in stacks]

    r = re.compile("move (.*) from (.*) to (.*)")
    instructions = [r.findall(line)[0] for line in instructions]
    instructions = [tuple(map(int, i)) for i in instructions]

    part1(stacks, instructions)
    part2(stacks, instructions)


def create_lists(stacks):
    lists = [list() for _ in range(9)]
    for line in list(reversed(stacks)):
        for i, c in line:
            lists[i - 1].append(c)
    return lists


def part1(stacks, instructions):
    lists = create_lists(stacks)
    for (count, frm, to) in instructions:
        for _ in range(count):
            lists[to - 1].append(lists[frm - 1].pop())
    print(''.join([li[-1] for li in lists]))


def part2(stacks, instructions):
    lists = create_lists(stacks)
    for (count, frm, to) in instructions:
        tmp = list()
        for _ in range(count):
            tmp.append(lists[frm - 1].pop())
        for _ in range(count):
            lists[to - 1].append(tmp.pop())
    print(''.join([li[-1] for li in lists]))


if __name__ == "__main__":
    main()
