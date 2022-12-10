from utils import read_input
from collections import defaultdict
import re


def main():
    dir_stack = [""]
    sizes = defaultdict(lambda: 0)

    total = 0
    i = read_input()

    size_re = re.compile("^([0-9]+) ")
    for line in i[1:]:
        if line.startswith("$ ls") or line.startswith("dir "):
            continue
        elif line.startswith("$ cd .."):
            dir_stack.pop()
        elif line.startswith("$ cd "):
            dir_stack.append(line[5:])
        else:
            total += int(size_re.findall(line)[0])
            for length in range(len(dir_stack), 0, -1):
                path = "/".join(dir_stack[:length])
                sizes[path] += int(size_re.findall(line)[0])

    print(sum({path: size for path, size in sizes.items() if size <= 100000}.values()))

    to_free = 30000000 - 70000000 + sizes[""]
    best = sizes[""]
    for space in sizes.values():
        if to_free < space < best:
            best = space
    print(best)


if __name__ == "__main__":
    main()
