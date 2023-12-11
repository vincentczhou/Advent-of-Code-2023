def main():
    with open("input") as input:
        grid = []

        # Insert Rows
        for line in input:
            line = line.strip()
            grid_line = []
            galaxy_exist = False
            for char in line:
                grid_line.append(char)
                if char == "#":
                    galaxy_exist = True
            grid.append(grid_line)
            if not galaxy_exist:
                grid.append(grid_line)

        # Insert Columns
        new_grid_cols = []
        for j in range(len(grid[0])):
            galaxy_exist = False
            for i in range(len(grid)):
                if grid[i][j] == "#":
                    galaxy_exist = True
            if not galaxy_exist:
                new_grid_cols.append(j)
        for shift, new_grid_col in enumerate(new_grid_cols):
            for line in grid:
                line.insert(new_grid_col + shift, ".")

        galaxy_locs = []
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "#":
                    galaxy_locs.append((row, col))

        sum = 0
        for i in range(len(galaxy_locs)):
            curr_galaxy = galaxy_locs[i]
            for j in range(i, len(galaxy_locs)):
                pair_galaxy = galaxy_locs[j]
                sum += abs(pair_galaxy[0] - curr_galaxy[0]) + \
                    abs(pair_galaxy[1] - curr_galaxy[1])

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 9799681
