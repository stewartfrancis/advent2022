from typing import List

from more_itertools import split_at
from utils import read_input


def main():
    lines = read_input()

    monkeys = parse_monkeys(lines)
    for i in range(20):
        round(monkeys, True)

    monkeys = parse_monkeys(lines)
    # For part 2 instead of storing the number, store the remainder from the perspective of each monkey
    bases = [monkey.divisor for monkey in monkeys.values()]
    for monkey in monkeys.values():
        monkey.items = [{base: item % base for base in bases} for item in monkey.items]

    for i in range(10000):
        round(monkeys, False)

    print(inspections(monkeys))


def parse_monkeys(lines):
    return {m.id: m for m in [Monkey(m) for m in split_at(lines, lambda x: x == '')]}


def inspections(monkeys):
    ins = [monkey.inspected for monkey in monkeys.values()]
    m1 = max(ins)
    ins.remove(m1)
    return m1 * max(ins)


def round(monkeys, is_part_1):
    # print(monkeys)
    for monkey in monkeys.values():
        inspected = monkey.inspect_items(is_part_1)
        # print(inspected)
        for item in inspected:
            monkeys[item[0]].items.append(item[1])


class Monkey:
    def __init__(self, m):
        self.id = int(m[0][7:-1])
        self.items: List = [int(i) for i in m[1][18:].split(", ")]
        match m[2][23:]:
            case "* old":
                self.operation = lambda x: x * x
            case o if "* " == o[:2]:
                self.operation = lambda x: x * int(o[2:])
            case _:
                self.operation = lambda x: x + int(o[2:])
        self.divisor = int(m[3][21:])
        self.true_monkey = int(m[4][29])
        self.false_monkey = int(m[5][30])
        self.inspected = 0

    def inspect_items(self, is_part_1):
        if is_part_1:
            new_items = [self.operation(item) // 3 for item in self.items]
            new_items = [(item, item % self.divisor == 0) for item in new_items]
        else:
            new_items = [  # Calculate new remainders for all monkey's divisors
                {base: self.operation(remainder) % base for base, remainder in item.items()}
                for item in self.items
            ]
            new_items = [(item, item[self.divisor] == 0) for item in new_items]
        self.items = []
        self.inspected += len(new_items)
        return [(self.true_monkey if item[1] else self.false_monkey, item[0]) for item in new_items]


if __name__ == '__main__':
    main()
