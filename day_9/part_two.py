def parse_line(line):
    full_hist = [line]
    curr_hist = []

    for i in range(len(line) - 1):
        curr_hist.append(line[i + 1] - line[i])
    full_hist.append(curr_hist)
    curr_hist = []
    while len(set(full_hist[-1])) != 1:
        for i in range(len(full_hist[-1]) - 1):
            curr_hist.append(full_hist[-1][i + 1] - full_hist[-1][i])
        full_hist.append(curr_hist)
        curr_hist = []

    for i in range(len(full_hist) - 2, -1, -1):
        full_hist[i].insert(0, full_hist[i][0] - full_hist[i + 1][0])
    return full_hist[0][0]


def main():
    with open("input") as input:
        lines = []
        for line in input:
            lines.append([int(num) for num in line.split()])

        sum = 0
        for line in lines:
            sum += parse_line(line)

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 1062
