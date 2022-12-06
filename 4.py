import re

from utils import read_input


def main():
    lines = read_input()
    r = re.compile("(.*)-(.*),(.*)-(.*)")
    ranges = map(lambda y: r.findall(y)[0], lines)
    ranges = [tuple(map(int, r)) for r in ranges]

    print(sum(map(encloses, ranges)))
    print(sum(map(overlaps, ranges)))


def overlaps(r):
    return (r[2] <= r[0] <= r[3]) or (r[2] <= r[1] <= r[3]) or encloses(r)


def encloses(r):
    return (r[0] <= r[2] and r[1] >= r[3]) or (r[2] <= r[0] and r[3] >= r[1])


if __name__ == "__main__":
    main()
