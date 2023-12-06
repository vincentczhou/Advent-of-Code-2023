
def process_range(range_, map):
    overlap_ranges = []
    nonoverlap = [range_]
    # Refactoring:
    # https://www.reddit.com/r/adventofcode/comments/18b4b0r/comment/kc2xy0p/
    # Same initial logic, but I overlooked the while loop
    # Necessary to check for overlaps in the leftover non-overlapped ranges per entry in map
    # Correct answer is still obtainable without, looking at the 2nd smallest minimum
    # But without is poor implementation, and obtaining the answer is due to chance (dependent on the dataset) 
    while nonoverlap:
        overlap = False
        curr = nonoverlap.pop()
        for new, start, length in map:
            curr_left = curr[0]
            curr_right = curr[1]
            map_left = start
            map_right = start + length
            overlap_left = max(curr_left, map_left)
            overlap_right = min(curr_right, map_right)

            if overlap_right > overlap_left:
                overlap = True
                overlap_ranges.append(
                    (overlap_left + (0 - start + new), overlap_right + (0 - start + new)))
                if curr_right > overlap_right:
                    nonoverlap.append((overlap_right, curr_right))
                if curr_left < overlap_left:
                    nonoverlap.append((curr_left, overlap_left))
                break
        if not overlap:
            overlap_ranges.append(curr)
    return overlap_ranges


def main():
    seed_list = []
    with open("input") as input:
        maps = []
        curr_map_array = []
        seed_list = []
        recording = False
        for line in input:
            line = line.strip()
            if line == "" and recording:
                recording = False
                maps.append(curr_map_array)
                curr_map_array = []
                continue
            if not recording:
                chunk = line.split(":")
                category = chunk[0].split(" ")[-1]
                if category == "seeds":
                    seed_list = [int(x) for x in chunk[1].strip().split(" ")]
                elif "map" in category:
                    recording = True
                    continue
            elif recording:
                curr_map_array.append(tuple([int(x) for x in line.split(" ")]))
        maps.append(curr_map_array)

        seed_ranges = []
        for i in range(0, len(seed_list), 2):
            seed_ranges.append((seed_list[i], seed_list[i] + seed_list[i + 1]))

        ranges = seed_ranges
        seed_ranges = []
        for map in maps:
            for range_ in ranges:
                seed_ranges += process_range(range_, map)
            ranges = seed_ranges
            seed_ranges = []

        print(f"The minimum is: {min(ranges)[0]}")


if __name__ == "__main__":
    main()

# The minimum is: 15290096
