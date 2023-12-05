def parse_line(line):
    chunk = line.strip().split(":")
    card_set = chunk[1].split("|")
    win_card = card_set[0].strip().split()
    my_card = card_set[1].strip().split()

    matches = 0

    for num in my_card:
        if num in win_card:
            matches += 1
    points = 0
    if matches > 0:
        points = pow(2, matches - 1)

    return points


def main():
    with open("input") as input:
        sum = 0
        for line in input:
            sum += parse_line(line)
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 17803
