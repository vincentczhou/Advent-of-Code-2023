multiplier = 1000000


def main():
    with open("input") as input:
        grid = []

        # Insert Rows
        new_grid_rows = []
        for row, line in enumerate(input):
            line = line.strip()
            grid_line = []
            galaxy_exist = False
            for char in line:
                grid_line.append(char)
                if char == "#":
                    galaxy_exist = True
            grid.append(grid_line)
            if not galaxy_exist:
                new_grid_rows.append(row)

        # Insert Columns
        new_grid_cols = []
        for j in range(len(grid[0])):
            galaxy_exist = False
            for i in range(len(grid)):
                if grid[i][j] == "#":
                    galaxy_exist = True
            if not galaxy_exist:
                new_grid_cols.append(j)

        galaxy_locs = []
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "#":
                    galaxy_locs.append((row, col))

        new_galaxy_locs = []
        for galaxy_loc in galaxy_locs:
            new_row = galaxy_loc[0]
            new_col = galaxy_loc[1]
            for new_grid_row in new_grid_rows:
                if galaxy_loc[0] > new_grid_row:
                    new_row += multiplier - 1
            for new_grid_col in new_grid_cols:
                if galaxy_loc[1] > new_grid_col:
                    new_col += multiplier - 1
            new_galaxy_locs.append((new_row, new_col))

        sum = 0
        for i in range(len(new_galaxy_locs)):
            curr_galaxy = new_galaxy_locs[i]
            for j in range(i, len(new_galaxy_locs)):
                pair_galaxy = new_galaxy_locs[j]
                sum += abs(pair_galaxy[0] - curr_galaxy[0]) + \
                    abs(pair_galaxy[1] - curr_galaxy[1])

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 513171773355
