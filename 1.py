from utils import read_input
from more_itertools import split_at

lines = read_input()

elf_item_cals = split_at(lines, lambda x: x == '')
elf_item_cals = [sum([int(item) for item in item_cals]) for item_cals in elf_item_cals]
by_cals = sorted(elf_item_cals, reverse=True)
print(by_cals[0])
print(sum(by_cals[:3]))
