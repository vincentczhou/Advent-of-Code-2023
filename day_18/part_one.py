def main():
    with open("input") as input:
        directions = []
        colors = []
        for line in input.read().split("\n"):
            chunk = line.split(" ")
            directions.append((chunk[0], int(chunk[1])))
            colors.append(chunk[2])

        boundary = 0

        coordinates = []
        d_map = {"L": (0, -1),
                 "R": (0, 1),
                 "U": (-1, 0),
                 "D": (1, 0)
                 }
        curr = [0, 0]
        for direction in directions:
            dir = d_map[direction[0]]
            multiplier = direction[1]
            boundary += multiplier
            m_dir = [i * multiplier for i in dir]
            n_dir = [i + j for i, j in zip(curr, m_dir)]

            coordinates.append(tuple(n_dir))
            curr = n_dir

        # Gauss's Area Formula
        coordinates.append(coordinates[0])
        area = 0
        for i in range(len(coordinates) - 1):
            area += (coordinates[i][0] * coordinates[i + 1][1]) - \
                (coordinates[i + 1][0] * coordinates[i][1])
        area = 0.5 * abs(area)

        # Pick's Theorem
        interior = (area + 1) - (boundary / 2)

        total = interior + boundary

        print(f"The total is: {int(total)}")


if __name__ == "__main__":
    main()

# The total is: 47045
