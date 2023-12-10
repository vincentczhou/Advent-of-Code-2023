import copy
from math import lcm

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

        # Brute-Force Solution
        # count = 0
        # curr_locs = [direction for direction in nodes.keys()
        #              if direction[-1] == "A"]
        # new_curr_locs = []
        # while steps:
        #     curr_dir = steps.pop(0)
        #     steps.append(curr_dir)
        #     for curr_loc in curr_locs:
        #         new_curr_locs.append(nodes[curr_loc][curr_dir])
        #     curr_locs = new_curr_locs
        #     new_curr_locs = []
        #     count += 1
        #     print(curr_locs)
        #     if all(direction[-1] == "Z" for direction in curr_locs):
        #         break

        # The problem statement does not verify that LCM would be viable.
        # However, the code below verifies that the period to reach each end node
        # is cyclic since the end node is always reached at the end of each instruction.
        # Therefore, we can conclude that LCM will work (although it really should not given the problem statement).
        curr_locs = [direction for direction in nodes.keys()
                     if direction[-1] == "A"]
        steps_original = copy.deepcopy(steps)
        counts_all = []
        for curr_loc in curr_locs:
            count = 0
            counts = []
            while steps:
                curr_dir = steps.pop(0)
                steps.append(curr_dir)
                curr_loc = nodes[curr_loc][curr_dir]
                count += 1
                if curr_loc[-1] == "Z":
                    counts.append(count)
                    count = 0
                    if len(counts) > 1 and counts[-1] == counts[0]:
                        break
            counts_all.append(counts)
            steps = copy.deepcopy(steps_original)

        print(
            f"Each path from a start to end node is cyclic: {all(counts[0] == counts[1] for counts in counts_all)}")

        counts_lcm = lcm(*[counts[0] for counts in counts_all])

        print(f"The count is: {counts_lcm}")


if __name__ == "__main__":
    main()

# Each path from a start to end node is cyclic: True
# The count is: 14299763833181
