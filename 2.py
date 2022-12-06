from utils import read_input


def main():
    lines = read_input()
    print(sum(map(rps, lines)))
    print(sum(map(ldw, lines)))


def rps(c):
    match c:
        case "A X": return 4
        case "B X": return 1
        case "C X": return 7
        case "A Y": return 8
        case "B Y": return 5
        case "C Y": return 2
        case "A Z": return 3
        case "B Z": return 9
        case "C Z": return 6


def ldw(c):
    match c:
        case "A X": return 3
        case "B X": return 1
        case "C X": return 2
        case "A Y": return 4
        case "B Y": return 5
        case "C Y": return 6
        case "A Z": return 8
        case "B Z": return 9
        case "C Z": return 7


if __name__ == "__main__":
    main()
