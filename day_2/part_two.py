def parse_line(line):
    chunk = line.strip().split(":")
    cube_sets = chunk[1].split(";")

    rgb = {"red": 0, "green": 0, "blue": 0}
    for set in cube_sets:
        color_sets = set.split(",")
        for color_set in color_sets:
            num_color_cube = color_set.strip().split(" ")
            num = int(num_color_cube[0])
            color = num_color_cube[1]
            if num > rgb[color]:
                rgb[color] = num

    prod = 1
    for value in rgb.values():
        prod = prod * value
    return prod


def main():
    with open("input") as input:
        sum = 0
        for line in input:
            sum += parse_line(line)
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 70265
