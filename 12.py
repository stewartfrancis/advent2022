from utils import read_input


def main():
    distances_forwards = [[worst for _ in row] for row in map]
    distances_forwards[start[0]][start[1]] = 0
    paths = [(start, 0)]
    while len(paths) > 0:
        paths = extend_paths(paths, lambda c, h: (map[c[0]][c[1]] - h) <= 1, distances_forwards)
    print(distances_forwards[end[0]][end[1]])

    distances_backwards = [[worst for _ in row] for row in map]
    distances_backwards[end[0]][end[1]] = 0
    paths = [(end, 0)]
    while len(paths) > 0:
        paths = extend_paths(paths, lambda c, h: (map[c[0]][c[1]] - h) >= -1, distances_backwards)
    print(min([distances_backwards[y][x] for y in range(y_len) for x in range(x_len) if map[y][x] == 1]))


def extend_paths(paths, legal_height, distances):
    new_paths = [extend_path(path, legal_height, distances) for path in paths]
    new_paths = [y for ys in new_paths for y in ys]  # flatten
    new_paths = list(filter(lambda p: distances[p[0][0]][p[0][1]] <= p[1], new_paths))  # filter longs
    return new_paths


def extend_path(path, legal_height, distances):
    (coord, distance) = path
    new_distance = distance + 1
    current_height = map[coord[0]][coord[1]]
    steps = [(coord[0] - 1, coord[1]), (coord[0], coord[1] + 1), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1)]
    steps = filter(lambda c: 0 <= c[0] < y_len and 0 <= c[1] < x_len, steps)  # in bounds
    steps = filter(lambda c: legal_height(c, current_height), steps)  # legal height
    steps = list(filter(lambda c: distances[c[0]][c[1]] > new_distance, steps))  # improved distance
    for step in steps:
        distances[step[0]][step[1]] = new_distance

    return [(step, new_distance) for step in steps]


def coords_of(c, lines):
    return [(i, line.index(c)) for i, line in filter(lambda line: c in line[1], enumerate(lines))][0]


lines = read_input()

start = coords_of("S", lines)
end = coords_of("E", lines)
map = [[ord(c) - 96 for c in line] for line in lines]
map[start[0]][start[1]] = 1
map[end[0]][end[1]] = 26
y_len = len(map)
x_len = len(map[0])
worst = y_len * x_len

if __name__ == '__main__':
    main()
