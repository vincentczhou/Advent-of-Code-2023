def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = input.read().split("\n")
        lines = [[char for char in line] for line in lines]

        start_col = next((i for i, chr in enumerate(lines[0]) if chr == "."))
        start = (0, start_col)
        end_col = next((i for i, chr in enumerate(lines[-1]) if chr == "."))
        end = (len(lines) - 1, end_col)

        directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1)
        }

        junctions = [start, end]
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if row < len(lines) - 1 and row >= 1 and col < len(lines[0]) - 1 and col >= 1 and lines[row][col] != "#":
                    count = 0
                    for direction, (drow, dcol) in directions.items():
                        nrow = row + drow
                        ncol = col + dcol
                        if lines[nrow][ncol] != "#":
                            count += 1
                    if count >= 3:
                        junctions.append((row, col))

        graph = {}
        for junction in junctions:
            s = []
            s.append(junction)
            visited = set()

            neighbors = {}
            dist = 0
            while s:
                curr = s.pop(-1)
                visited.add(curr)
                if curr != junction:
                    dist += 1
                    if curr in junctions:
                        neighbors[curr] = dist
                        dist = 0
                        continue
                for direction, (drow, dcol) in directions.items():
                    crow, ccol = curr
                    nrow = crow + drow
                    ncol = ccol + dcol
                    if nrow < len(lines) and nrow >= 0 and ncol < len(lines[0]) and ncol >= 0 and lines[nrow][ncol] != "#" and (nrow, ncol) not in visited:
                        s.append((nrow, ncol))
            graph[junction] = neighbors

        distances = []
        seen = set()

        def dfs(p, distance):
            if p == end:
                distances.append(distance)

            seen.add(p)
            for neighbor, dist in graph[p].items():
                if neighbor not in seen:
                    dfs(neighbor, distance + dist)
            seen.remove(p)

        dfs(start, 0)

        print(f"The maximum is {max(distances)}")


if __name__ == "__main__":
    main()

# The maximum is 6534
