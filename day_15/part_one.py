def hash_algo(s):
    curr_v = 0
    for char in s:
        curr_v += ord(char)
        curr_v *= 17
        curr_v = curr_v % 256
    return curr_v


def main():
    with open("input") as input:
        steps = input.read().split(",")

        total = 0
        for step in steps:
            total += hash_algo(step)

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 510013
