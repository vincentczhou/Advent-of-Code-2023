def check_valid(spring, pattern):
    valid = True
    curr_p = 0
    recording = 0
    for char in spring:
        if char == "#":
            recording += 1
        elif recording > 0 and recording != pattern[curr_p]:
            valid = False
            break
        elif recording > 0 and recording == pattern[curr_p]:
            curr_p += 1
            recording = 0
    if recording > 0 and recording != pattern[curr_p]:
        valid = False
    return valid


def map_spring(spring, perm):
    locs = [i for i in range(len(spring)) if spring[i] == "?"]
    mapped_spring = spring.copy()
    for loc, char in zip(locs, perm):
        mapped_spring[loc] = char
    return mapped_spring


def dist_perm_gen(perm_list, s_arr, start, end):
    if start == end:
        perm_list.append("".join(s_arr))
    for i in range(start, end):
        # Check if char has already been swapped in a previous instance of this for loop
        if s_arr[i] not in s_arr[start:i]:
            new_arr = s_arr.copy()
            original = new_arr[start]
            new_arr[start] = new_arr[i]
            new_arr[i] = original
            dist_perm_gen(perm_list, new_arr, start + 1, end)


def distinct_permutations(s):
    s_arr = [char for char in s]
    perm_list = []
    dist_perm_gen(perm_list, s_arr, 0, len(s))
    return perm_list


def main():
    with open("input") as input:
        springs = []
        patterns = []
        for line in input:
            chunk = line.strip().split(" ")
            springs.append([char for char in chunk[0]])
            patterns.append([int(num) for num in chunk[1].split(",")])

        total = 0
        for spring, pattern in zip(springs, patterns):
            valid_count = 0
            available = sum(pattern) - spring.count("#")
            spots = spring.count("?")

            perm_string = "".join(["#"] * available) + \
                "".join(["."] * (spots - available))
            perm_set = distinct_permutations(perm_string)

            for perm in perm_set:
                mapped_spring = map_spring(spring, perm)
                if check_valid(mapped_spring, pattern):
                    valid_count += 1
            total += valid_count

        print(f"The sum is: {total}")


if __name__ == "__main__":
    main()

# The sum is: 7307
