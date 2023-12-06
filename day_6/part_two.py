def main():
    with open("input") as input:
        lines = []
        for line in input:
            chunk = line.strip().split(":")
            real_race = "".join(chunk[1].strip().split())
            lines.append(int(real_race))
        time = lines[0]
        distance = lines[1]

        # Revised Math Approach
        count = 0
        middle = (time + 1) // 2
        for j in range(middle, 0, -1):
            curr_distance = j * (time - j)
            if curr_distance <= distance:
                count += (middle - 1 - j) * 2
                if (time % 2) == 0:
                    count += 1
                break

        print(f"The sum is: {count}")


if __name__ == "__main__":
    main()

# The sum is: 23654842
