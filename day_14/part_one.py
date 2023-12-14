def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = []
        for line in input.readlines():
            lines.append([char for char in line.strip()])

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

        total = 0
        for i in range(len(lines)):
            count = 0
            for j in range(len(lines[0])):
                if lines[i][j] == "O":
                    count += 1
            total += count * (len(lines) - i)

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 113456
