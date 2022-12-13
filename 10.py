from utils import read_input
from collections import deque
from itertools import count
from more_itertools import chunked


def main():
    lines = read_input()

    cycles = list(cycle_generator(lines))
    print(sum([c[0] * c[1] for c in filter(lambda c: (c[0] + 20) % 40 == 0, cycles)]))

    pixels = zip([p % 40 for p in range(0, 240)], [{c[1] - 1, c[1], c[1] + 1} for c in cycles])
    for row in chunked(("#" if p[0] in p[1] else "." for p in pixels), 40):
        print("".join(row))


def cycle_generator(lines):
    instructions = deque(lines)
    x = 1
    busy_until = (0, 0)
    for cycle in count(1, 1):
        yield cycle, x
        if busy_until[0] == cycle:
            x += busy_until[1]
        elif busy_until[0] > cycle:
            pass
        elif len(instructions) == 0:
            if busy_until[0] > cycle:
                pass
            else:
                break
        else:
            instruction = instructions.popleft()
            if instruction[:4] == "noop":
                pass
            else:
                busy_until = cycle + 1, int(instruction[5:])


if __name__ == "__main__":
    main()
