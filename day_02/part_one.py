limits = {"red": 12, "green": 13, "blue": 14}


def parse_line(line):
    chunk = line.strip().split(":")
    id = int(chunk[0].split(" ")[-1])
    cube_sets = chunk[1].split(";")

    for set in cube_sets:
        color_sets = set.split(",")
        for color_set in color_sets:
            num_color_cube = color_set.strip().split(" ")
            num = int(num_color_cube[0])
            color = num_color_cube[1]
            if num > limits[color]:
                id = 0

    # Woops! Answers a different question...
    # If the cumulative number (summation) of cubes used in each
    # Game (not round) falls within the limit

    # rgb = {"red": 0, "green": 0, "blue": 0}
    # for set in cube_sets:
    #     color_sets = set.split(",")
    #     for color_set in color_sets:
    #         num_color_cube = color_set.strip().split(" ")
    #         num = int(num_color_cube[0])
    #         color = num_color_cube[1]
    #         rgb[color] += num

    # for key in rgb.keys():
    #     if rgb[key] > limits[key]:
    #         id = 0

    return id


def main():
    with open("input") as input:
        sum = 0
        for line in input:
            sum += parse_line(line)
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 2505
