import functools


@functools.cache
def recursion(spring, pattern, curr_p):
    if len(spring) == 0 and curr_p == len(pattern):
        return 1
    elif len(spring) == 0:
        return 0

    sum = 0
    if spring[0] == ".":
        sum += recursion(spring[1:], pattern, curr_p)
    elif spring[0] == "?":
        sum += recursion("#" + spring[1:], pattern, curr_p)
        sum += recursion("." + spring[1:], pattern, curr_p)
    elif spring[0] == "#":
        if curr_p >= len(pattern):
            return 0
        if len(spring) < pattern[curr_p]:
            return 0

        if all(char == "#" or char == "?" for char in spring[:pattern[curr_p]]) and len(spring) == pattern[curr_p]:
            return recursion("", pattern, curr_p + 1)
        elif all(char == "#" or char == "?" for char in spring[:pattern[curr_p]]) and (spring[pattern[curr_p]] == "." or spring[pattern[curr_p]] == "?"):
            return recursion("." + spring[pattern[curr_p] + 1:], pattern, curr_p + 1)
        else:
            return 0

    return sum


def main():
    with open("input") as input:
        springs = []
        patterns = []
        for line in input:
            chunk = line.strip().split(" ")
            spring = chunk[0]
            multiplied_spring = ""
            pattern = [int(num) for num in chunk[1].split(",")]

            for i in range(0, 4):
                multiplied_spring += spring
                multiplied_spring += "?"
            multiplied_spring += spring

            springs.append(multiplied_spring)
            patterns.append([int(num) for num in chunk[1].split(",")] * 5)

        total = 0
        for spring, pattern in zip(springs, patterns):
            valid_count = recursion(spring, tuple(pattern), 0)
            total += valid_count

        print(f"The sum is: {total}")


if __name__ == "__main__":
    main()

# The sum is: 3415570893842
