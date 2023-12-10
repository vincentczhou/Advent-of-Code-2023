def main():
    with open("input") as input:
        lines = []
        for line in input:
            chunk = line.strip().split(":")
            lines.append([int(x) for x in chunk[1].strip().split()])
        times = lines[0]
        distances = lines[1]
        counts = []

        # Brute Force Approach
        # for i, time in enumerate(times):
        #     distance = distances[i]
        #     count = 0
        #     for j in range(time + 1):
        #         curr_distance = j * (time - j)
        #         if curr_distance > distance:
        #             count += 1
        #     counts.append(count)

        # Math Approach
        # for i, time in enumerate(times):
        #     distance = distances[i]
        #     count = 0
        #     middle = (time + 1) // 2
        #     for j in range(time + 1):
        #         curr_distance = j * (time - j)
        #         if curr_distance > distance:
        #             count += (middle - j) * 2
        #             if (time % 2) == 0:
        #                 count += 1
        #             counts.append(count)
        #             break

        # Revised Math Appraoch
        for i, time in enumerate(times):
            distance = distances[i]
            count = 0
            middle = (time + 1) // 2
            for j in range(middle, 0, -1):
                curr_distance = j * (time - j)
                if curr_distance <= distance:
                    count += (middle - 1 - j) * 2
                    if (time % 2) == 0:
                        count += 1
                    counts.append(count)
                    break

        sum = 1
        for count in counts:
            sum = sum * count

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 303600
