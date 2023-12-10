left_options = ["-", "L", "F", "S"]
right_options = ["-", "J", "7", "S"]

up_options = ["|", "F", "7", "S"]
down_options = ["|", "L", "J", "S"]

left_routes = ["-", "J", "7", "S"]
right_routes = ["-", "F", "L", "S"]

up_routes = ["|", "L", "J", "S"]
down_routes = ["|", "F", "7", "S"]


def peek_left(curr_loc, graph):
    left = False
    curr_node = graph[curr_loc[0]][curr_loc[1]]
    if not curr_loc[1] == 0 and graph[curr_loc[0]][curr_loc[1] - 1] in left_options and curr_node in left_routes:
        left = True
    return left


def peek_right(curr_loc, graph):
    right = False
    curr_node = graph[curr_loc[0]][curr_loc[1]]
    if not curr_loc[1] == (len(graph[0]) - 1) and graph[curr_loc[0]][curr_loc[1] + 1] in right_options and curr_node in right_routes:
        right = True
    return right


def peek_up(curr_loc, graph):
    up = False
    curr_node = graph[curr_loc[0]][curr_loc[1]]
    if not curr_loc[0] == 0 and graph[curr_loc[0] - 1][curr_loc[1]] in up_options and curr_node in up_routes:
        up = True
    return up


def peek_down(curr_loc, graph):
    down = False
    curr_node = graph[curr_loc[0]][curr_loc[1]]
    if not curr_loc[0] == (len(graph) - 1) and graph[curr_loc[0] + 1][curr_loc[1]] in down_options and curr_node in down_routes:
        down = True
    return down


def main():
    with open("input") as input:
        graph = []
        s_loc = None
        for row, line in enumerate(input):
            curr_row = []
            for col, char in enumerate(line.strip()):
                if char == "S":
                    s_loc = (row, col)
                curr_row.append(char)
            graph.append(curr_row)

        visited = []

        curr_loc = s_loc
        visited.append(curr_loc)
        if peek_left(curr_loc, graph):
            curr_loc = (curr_loc[0], curr_loc[1] - 1)
        elif peek_right(curr_loc, graph):
            curr_loc = (curr_loc[0], curr_loc[1] + 1)
        elif peek_up(curr_loc, graph):
            curr_loc = (curr_loc[0] - 1, curr_loc[1])
        elif peek_down(curr_loc, graph):
            curr_loc = (curr_loc[0] + 1, curr_loc[1])

        curr_node = graph[curr_loc[0]][curr_loc[1]]
        visited.append(curr_loc)
        counter = 1
        while curr_node != "S":
            if peek_left(curr_loc, graph) and (curr_loc[0], curr_loc[1] - 1) not in visited:
                curr_loc = (curr_loc[0], curr_loc[1] - 1)
            elif peek_right(curr_loc, graph) and (curr_loc[0], curr_loc[1] + 1) not in visited:
                curr_loc = (curr_loc[0], curr_loc[1] + 1)
            elif peek_up(curr_loc, graph) and (curr_loc[0] - 1, curr_loc[1]) not in visited:
                curr_loc = (curr_loc[0] - 1, curr_loc[1])
            elif peek_down(curr_loc, graph) and (curr_loc[0] + 1, curr_loc[1]) not in visited:
                curr_loc = (curr_loc[0] + 1, curr_loc[1])
            else:
                curr_loc = s_loc
            curr_node = graph[curr_loc[0]][curr_loc[1]]
            visited.append(curr_loc)
            counter += 1

        visited.pop(0)
        print(f"The count is: {counter // 2}")


if __name__ == "__main__":
    main()

# The count is: 6947
