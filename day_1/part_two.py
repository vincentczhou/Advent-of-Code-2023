
whitelist = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1,
             "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def parse_line(line):
    first_num = 0
    first_num_index = len(line) + 1337
    last_num = 0
    last_num_index = -1337
    for key in whitelist.keys():
        first_index_match = line.find(key)
        last_index_match = line.rfind(key)
        # Case 1: Key not present
        if first_index_match == -1:
            continue
        # First key found will initialize both first and last
        # All subsequent keys found will either fall under Case 2 or Case 3
        # But not both - first_index_match is less than first,
        # Or last_index_match is greater than last (need to account for multiple instaces of same match)
        # Case 2: Replace first
        if first_index_match < first_num_index:
            first_num = whitelist[key]
            first_num_index = first_index_match
        # Case 3: Replace last
        if last_index_match > last_num_index:
            last_num = whitelist[key]
            last_num_index = last_index_match
    return int(f"{first_num}{last_num}")


def main():
    with open("input") as input:
        sum = 0
        for line in input:
            sum += parse_line(line)
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 54845
