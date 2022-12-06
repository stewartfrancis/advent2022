from utils import read_input
from more_itertools import windowed


def main():
    stream = read_input()[0]
    find_marker(stream, 4)
    find_marker(stream, 14)


def find_marker(stream, l):
    windows = windowed(stream, l)
    windows = map(set, windows)
    windows = enumerate(windows, l)
    for (i, s) in windows:
        if len(s) == l:
            print(i)
            break


if __name__ == "__main__":
    main()
