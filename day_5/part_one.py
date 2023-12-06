def main():
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

        minimum = None
        for seed in seed_list:
            location = seed
            for map in maps:
                for entry in map:
                    if location < entry[1] + entry[2] and location >= entry[1]:
                        location = location - entry[1] + entry[0]
                        break
            if minimum is None or location < minimum:
                minimum = location

        print(f"The minimum is: {minimum}")


if __name__ == "__main__":
    main()

# The minimum is: 424490994
