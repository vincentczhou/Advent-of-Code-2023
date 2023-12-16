import sys
sys.setrecursionlimit(5000)


def recursion(row, col, drow, dcol, lines, visited):
    curr = (row, col, drow, dcol)
    # Two Base Cases
    # 1. Light exits edges of grid
    # 2. Light starts looping, in which case it doesn't necessarily stop on
    #    a tile that's been visited (since direction matters), but on the inevitable
    #    case where (inevitable given that it is looping) the [tile and same direction] have been 'visited' before
    if not (row > (len(lines) - 1) or row < 0 or col > (len(lines[0]) - 1) or col < 0) and curr not in visited:
        visited.add(curr)
        match lines[row][col]:
            case ".":
                recursion(row + drow, col + dcol, drow, dcol, lines, visited)
            case "/":
                if drow == 1 and dcol == 0:
                    recursion(row, col - 1, 0, -1, lines, visited)
                elif drow == -1 and dcol == 0:
                    recursion(row, col + 1, 0, 1, lines, visited)
                elif drow == 0 and dcol == 1:
                    recursion(row - 1, col, -1, 0, lines, visited)
                elif drow == 0 and dcol == -1:
                    recursion(row + 1, col, 1, 0, lines, visited)
            case "\\":
                if drow == 1 and dcol == 0:
                    recursion(row, col + 1, 0, 1, lines, visited)
                elif drow == -1 and dcol == 0:
                    recursion(row, col - 1, 0, -1, lines, visited)
                elif drow == 0 and dcol == 1:
                    recursion(row + 1, col, 1, 0, lines, visited)
                elif drow == 0 and dcol == -1:
                    recursion(row - 1, col, -1, 0, lines, visited)
            case "|":
                if (drow == 1 or drow == -1) and dcol == 0:
                    recursion(row + drow, col + dcol,
                              drow, dcol, lines, visited)
                elif drow == 0 and (dcol == 1 or dcol == -1):
                    recursion(row - 1, col, -1, 0, lines, visited)
                    recursion(row + 1, col, 1, 0, lines, visited)
            case "-":
                if drow == 0 and (dcol == 1 or dcol == -1):
                    recursion(row + drow, col + dcol,
                              drow, dcol, lines, visited)
                elif (drow == 1 or drow == -1) and dcol == 0:
                    recursion(row, col - 1, 0, -1, lines, visited)
                    recursion(row, col + 1, 0, 1, lines, visited)


def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = input.read().split("\n")
        lines = [[char for char in line] for line in lines]

        visited = set()

        recursion(0, 0, 0, 1, lines, visited)

        dup = 0
        for visit in visited:
            if lines[visit[0]][visit[1]] == "#":
                dup += 1
            lines[visit[0]][visit[1]] = "#"

        total = len(visited) - dup

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 7728
