from queue import PriorityQueue


class Node:
    def __init__(self, heat, sdist, row, col, direction=None, dir_count=0, visited=False, prev=None):
        self.heat = heat
        self.sdist = sdist
        self.row = row
        self.col = col
        self.direction = direction
        self.dir_count = dir_count
        self.visited = visited
        self.prev = prev

    def __eq__(self, other):
        return (self.sdist == other.sdist) and (self.row == other.row) and (self.col == other.col)

    def __lt__(self, other):
        return (self.sdist < other.sdist)

    def __gt__(self, other):
        return (self.sdist > other.sdist)

    def __le__(self, other):
        return (self.sdist < other.sdist) or (self.sdist == other.sdist)

    def __ge__(self, other):
        return (self.sdist > other.sdist) or (self.sdist == other.sdist)

    def __repr__(self):
        return f"{self.row} {self.col} {self.direction} {self.dir_count}"


def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        lines = input.read().split("\n")
        lines = [[int(char) for char in line] for line in lines]
        max_val = sum([sum(line) for line in lines])

        # 4D Graph Traversal!!!

        nodes = []
        for row, line in enumerate(lines):
            node = []
            for col, char in enumerate(line):
                nod = []
                for direction in ["down", "up", "right", "left"]:
                    no = []
                    for count in range(0, 3):
                        no.append(Node(char, max_val, row, col,
                                  direction=direction, dir_count=count))
                    nod.append(no)
                node.append(nod)
            nodes.append(node)

        dir_map = {
            "down": 0,
            "up": 1,
            "right": 2,
            "left": 3
        }
        directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1)
        }

        pq = PriorityQueue()
        start = Node(0, 0, 0, 0, direction="initial", dir_count=0)
        start.prev = start
        pq.put(start)

        while not pq.empty():
            curr_node = pq.get()
            if not curr_node.visited:
                curr_node.visited = True
                for direction, (drow, dcol) in directions.items():
                    dc = curr_node.dir_count
                    if direction == curr_node.direction:
                        dc += 1
                    else:
                        dc = 0
                    nrow = curr_node.row + drow
                    ncol = curr_node.col + dcol

                    if nrow < len(lines) and nrow >= 0 and ncol < len(lines[0]) and ncol >= 0 and not (nrow == curr_node.prev.row and ncol == curr_node.prev.col) and dc < 3:
                        next_node = nodes[nrow][ncol][dir_map[direction]][dc]
                        new_sdist = curr_node.sdist + next_node.heat
                        if new_sdist < next_node.sdist:
                            next_node.sdist = new_sdist
                            next_node.prev = curr_node
                            next_node.direction = direction
                            next_node.dir_count = dc
                            pq.put(next_node)

        heats = []
        for d in nodes[len(lines) - 1][len(lines[0]) - 1]:
            for n in d:
                heats.append(n.sdist)
        print(f"The minimum is {min(heats)}")


if __name__ == "__main__":
    main()

# The minimum is 1128
