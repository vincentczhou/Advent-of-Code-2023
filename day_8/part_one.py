mapping = {"L": 0, "R": 1}


def main():
    with open("input") as input:
        nodes = {}
        read_input = input.read().split("\n\n")
        steps = [mapping[char] for char in read_input[0]]
        for line in read_input[1].split("\n"):
            chunk = line.strip().split("=")
            node = chunk[0].strip()
            directions = [direction.strip()
                          for direction in chunk[1].strip()[1:-1].split(",")]
            nodes[node] = tuple(directions)

        count = 0
        curr_loc = "AAA"
        while steps:
            curr_dir = steps.pop(0)
            steps.append(curr_dir)
            curr_loc = nodes[curr_loc][curr_dir]
            count += 1
            if curr_loc == "ZZZ":
                break

        print(f"The count is: {count}")


if __name__ == "__main__":
    main()

# The sum is: 18157
