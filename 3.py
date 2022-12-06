from typing import List
from more_itertools import chunked

from utils import read_input


def main():
    backpacks: List[str] = read_input()

    containers = [(b[0:len(b) // 2], b[len(b) // 2:]) for b in backpacks]
    dups = [next(iter(set(b[0]).intersection(set(b[1])))) for b in containers]
    print(sum(map(score, dups)))

    grouped = chunked([set(b) for b in backpacks], 3)
    badges = [next(iter(group[0].intersection(group[1]).intersection(group[2]))) for group in grouped]
    print(sum(map(score, badges)))


def score(c):
    o = ord(c)
    if o > 96:
        return o - 96
    else:
        return o - 38


if __name__ == "__main__":
    main()
