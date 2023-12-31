from queue import PriorityQueue


def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = input.read().split("\n")
        lines = [[char for char in line] for line in lines]

        start_col = next((i for i, chr in enumerate(lines[0]) if chr == "."))
        start = (-1, 0, start_col)
        end_col = next((i for i, chr in enumerate(lines[-1]) if chr == "."))

        min_val = -1 * (len(lines[0]) * len(lines)) ** 2
        dist = [[min_val for char in line] for line in lines]
        dist[start[1]][start[2]] = 0

        prev = [[None for char in line] for line in lines]
        prev[start[1]][start[2]] = (start[1], start[2])

        directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1)
        }

        d_arrow = {
            "v": "down",
            "^": "up",
            ">": "right",
            "<": "left"
        }

        pq = PriorityQueue()
        visited = set()
        pq.put(start)

        while not pq.empty():
            curr_node = pq.get()
            curr_node_loc = (curr_node[1], curr_node[2])
            # if curr_node_loc not in visited:
            visited.add(curr_node_loc)
            for direction, (drow, dcol) in directions.items():
                crow = curr_node[1]
                ccol = curr_node[2]
                nrow = crow + drow
                ncol = ccol + dcol
                if nrow < len(lines) and nrow >= 0 and ncol < len(lines[0]) and ncol >= 0 and lines[nrow][ncol] != "#" and ((nrow, ncol) != prev[crow][ccol]) and (lines[nrow][ncol] not in d_arrow.keys() or d_arrow[lines[nrow][ncol]] == direction):
                    new_dist = dist[crow][ccol] + 1
                    if new_dist > dist[nrow][ncol]:
                        dist[nrow][ncol] = new_dist
                        prev[nrow][ncol] = (crow, ccol)
                        pq.put((-1 * new_dist, nrow, ncol))

        print(f"The maximum is {dist[-1][end_col]}")


if __name__ == "__main__":
    main()

# The maximum is 2430
