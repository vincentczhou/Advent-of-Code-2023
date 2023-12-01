def main():
    with open("input") as input:
        sum = 0
        for line in input:
            first_num = ""
            last_num = ""
            for char in line:
                if not first_num and char.isdigit():
                    first_num = char
                    last_num = char
                elif char.isdigit():
                    last_num = char
            sum += int(first_num + last_num)
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 55090
