from utils import read_input


def main():
    lines = read_input()

    def move(p, n):
        y_diff = p[0] - n[0]
        x_diff = p[1] - n[1]
        n2y = int(y_diff / 2)
        n2x = int(x_diff / 2)
        if n2y == 0 and n2x != 0:
            d = y_diff, n2x
        elif n2x == 0 and n2y != 0:
            d = n2y, x_diff
        else:
            d = n2y, n2x
        return n[0] + d[0], n[1] + d[1]

    def run(length):
        nonlocal lines

        knots = [(0, 0) for _ in range(0, length)]
        tail_visited = set()
        tail_visited.add(knots[-1])

        for line in lines:
            direction = line[0]
            distance = int(line[2:])

            for i in range(0, distance):
                if direction == "U":
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                elif direction == "D":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                elif direction == "L":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                else:
                    knots[0] = (knots[0][0], knots[0][1] + 1)

                for j in range(1, len(knots)):
                    knots[j] = move(knots[j - 1], knots[j])

                tail_visited.add(knots[-1])

        return len(tail_visited)

    print(run(2))
    print(run(10))


if __name__ == "__main__":
    main()
