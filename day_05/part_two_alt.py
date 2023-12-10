import pandas as pd
import pyranges as pr


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

        df_seed = pd.DataFrame(seed_ranges, columns=["Start", "End"])
        df_seed["Chromosome"] = "aoc"
        pr_seed = pr.PyRanges(df_seed)

        pr_maps = []
        for map in maps:
            df = pd.DataFrame(map, columns=["dest", "Start", "range"])
            df["End"] = df["Start"] + df["range"]
            df["Chromosome"] = "aoc"
            pr_df = pr.PyRanges(df)
            pr_maps.append(pr_df)

        for pr_map in pr_maps:
            intersect = pr_seed.intersect(pr_map).join(pr_map, how="left")
            # non_intersect = pr_seed.intersect(
            #     pr_map, invert=True).join(pr_map, how="left")
            # Returns intervals without overlaps - does not inclue subintervals
            non_intersect = pr_seed.subtract(
                intersect).join(pr_map, how="left")
            df_seed = pd.concat([intersect.df, non_intersect.df])
            df_seed = df_seed.replace(-1, 0)
            df_seed["Start"] = df_seed["Start"] - \
                df_seed["Start_b"] + df_seed["dest"]
            df_seed["End"] = df_seed["End"] - \
                df_seed["Start_b"] + df_seed["dest"]
            df_seed = df_seed[["Chromosome", "Start", "End"]]
            pr_seed = pr.PyRanges(df_seed)

        print(f"The minimum is: {df_seed['Start'].min()}")


if __name__ == "__main__":
    main()

# The minimum is: 15290096
