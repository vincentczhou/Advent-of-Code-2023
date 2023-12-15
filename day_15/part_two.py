from collections import OrderedDict


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

        boxes = [OrderedDict() for i in range(256)]
        for step in steps:
            if step[-1] == "-":
                label = step[:-1]
                if label in boxes[hash_algo(label)].keys():
                    boxes[hash_algo(label)].pop(label)
            elif "=" in step:
                chunk = step.split("=")
                label = chunk[0]
                lens = int(chunk[1])
                boxes[hash_algo(label)][label] = lens

        total = 0
        for i, box in enumerate(boxes):
            for j, val in enumerate(box.values()):
                total += (i + 1) * (j + 1) * val

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 268497
