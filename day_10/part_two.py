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

        s_pipe = "S"
        if peek_left(s_loc, graph) and peek_right(s_loc, graph):
            s_pipe = "-"
        elif peek_up(s_loc, graph) and peek_down(s_loc, graph):
            s_pipe = "|"
        elif peek_left(s_loc, graph) and peek_up(s_loc, graph):
            s_pipe = "J"
        elif peek_left(s_loc, graph) and peek_down(s_loc, graph):
            s_pipe = "7"
        elif peek_right(s_loc, graph) and peek_up(s_loc, graph):
            s_pipe = "L"
        elif peek_right(s_loc, graph) and peek_down(s_loc, graph):
            s_pipe = "F"
        graph[s_loc[0]][s_loc[1]] = s_pipe

        # Ray-Casting Algorithm
        # Drawing rays to the right, valid line intersections will be at "|", "L7", and "FJ"

        # Bounding Box

        row_min = min(visited)[0]
        row_max = max(visited)[0]
        col_min = min(visited, key=lambda x: x[1])[1]
        col_max = max(visited, key=lambda x: x[1])[1]

        tile = 0
        for row in range(row_min + 1, row_max):
            for col in range(col_min + 1, col_max):
                curr_loc = (row, col)
                if curr_loc in visited:
                    continue

                touch_num = 0
                touches = []
                for side in range(col + 1, col_max + 1):
                    if (row, side) in visited:
                        touches.append(graph[row][side])
                        if (graph[row][side]) == "S":
                            touches[-1] = "L"

                prev_pipe = None
                prev_pipe_map = {"L": "7", "F": "J"}
                for pipe in touches:
                    if pipe == "-":
                        continue
                    elif pipe == "|":
                        touch_num += 1
                    elif prev_pipe and pipe == prev_pipe_map[prev_pipe]:
                        touch_num += 1
                        prev_pipe = None
                    elif prev_pipe and pipe != prev_pipe_map[prev_pipe]:
                        prev_pipe = None
                    elif pipe == "L" or pipe == "F":
                        prev_pipe = pipe
                if touch_num % 2 == 1:
                    tile += 1

        print(f"The count is: {tile}")


if __name__ == "__main__":

    main()
# The count is: 273
