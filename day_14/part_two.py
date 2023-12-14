cycles = 1000000000


def north(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                loc = i
                for k in range(i, 0, -1):
                    if lines[k - 1][j] == ".":
                        loc = k - 1
                    else:
                        break
                lines[i][j] = "."
                lines[loc][j] = "O"


def west(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                loc = j
                for k in range(j, 0, -1):
                    if lines[i][k - 1] == ".":
                        loc = k - 1
                    else:
                        break
                lines[i][j] = "."
                lines[i][loc] = "O"


def south(lines):
    for i in range(len(lines) - 1, -1, -1):
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                loc = i
                for k in range(i, len(lines) - 1):
                    if lines[k + 1][j] == ".":
                        loc = k + 1
                    else:
                        break
                lines[i][j] = "."
                lines[loc][j] = "O"


def east(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1, -1, -1):
            if lines[i][j] == "O":
                loc = j
                for k in range(j, len(lines[0]) - 1):
                    if lines[i][k + 1] == ".":
                        loc = k + 1
                    else:
                        break
                lines[i][j] = "."
                lines[i][loc] = "O"


def calc_total(lines):
    total = 0
    for i in range(len(lines)):
        count = 0
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                count += 1
        total += count * (len(lines) - i)
    return total


def lines_to_str(lines):
    final = ""
    for line in lines:
        final += "".join(line)
    return final


def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = []
        for line in input.readlines():
            lines.append([char for char in line.strip()])

        # Initially solved by manually identifying the cycle (period) length, then doing modulo
        # The approach below finds the instance of the 'grid' when it is first repeated,
        # so it identifies the second instance of the cycle's beginning/first instance of the cycle's end (but uses the same logic as my initial manual approach)
        seen_grids = []
        seen_totals = []
        start_idx = 0
        period = 0
        for i in range(cycles):
            north(lines)
            west(lines)
            south(lines)
            east(lines)
            curr_grid = lines_to_str(lines)
            if curr_grid in seen_grids:
                start_idx = seen_grids.index(curr_grid)
                period = i - start_idx
                break
            else:
                seen_grids.append(curr_grid)
                seen_totals.append(calc_total(lines))
        cycle_grid_idx = ((cycles - 1 - start_idx) % period) + start_idx
        total = seen_totals[cycle_grid_idx]

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 118747
