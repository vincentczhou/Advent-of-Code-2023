symbols = ["*"]


def main():
    sum = 0
    with open("input") as input:
        nums = []
        nums_locs = []
        sym_locs = []

        for row, line in enumerate(input):
            digits = []
            recording_number = False
            for col, char in enumerate(line):
                if char.isdigit() and recording_number:
                    digits.append(char)
                elif char.isdigit() and not recording_number:
                    digits.append(char)
                    recording_number = True
                    nums_locs.append((row, col))  # Start of digit location
                elif digits:
                    recording_number = False
                    nums.append(int("".join(digits)))
                    digits.clear()

                if char in symbols:
                    sym_locs.append((row, col))

        gear_values = {k: [] for k in sym_locs}

        for i, nums_loc in enumerate(nums_locs):
            for sym_loc in sym_locs:
                row_range = (sym_loc[0] - 1, sym_loc[0] + 1)
                if not (nums_loc[0] <= row_range[1] and nums_loc[0] >= row_range[0]):
                    continue
                col_range = (nums_loc[1] - 1, nums_loc[1] + len(str(nums[i])))
                if not (sym_loc[1] <= col_range[1] and sym_loc[1] >= col_range[0]):
                    continue
                gear_values[sym_loc].append(nums[i])

        for value in gear_values.values():
            if len(value) == 2:
                sum += (value[0] * value[1])

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 86879020
