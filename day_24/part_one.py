import numpy as np
np.seterr(all="raise")


lower_bound = 200000000000000
upper_bound = 400000000000000


def line_intersect(pos_a, dir_a, pos_b, dir_b):
    coefficient = np.array([[t, -s] for t, s in zip(dir_a, dir_b)][:-1])
    ordinate = np.array([0 - a + b for a, b in zip(pos_a, pos_b)][:-1])
    t = None
    ret = None
    try:
        t = np.linalg.solve(coefficient, ordinate)
        if pos_a[-1] + dir_a[-1] * t[0] == pos_b[-1] + dir_b[-1] * t[1] and np.all(t >= 0):
            ret = np.array(pos_a) + np.array(dir_a) * t[0]
    except Exception as e:
        pass
    return ret


def main():
    with open("input") as input:
        pos = []
        dir = []
        for line in input.read().split("\n"):
            p, d = line.split("@")
            pos.append(tuple([int(x) for x in p.split(",")]))
            dir.append(tuple([int(x) for x in d.split(",")]))

        pos = [(x, y, 0) for x, y, z in pos]
        dir = [(x, y, 0) for x, y, z in dir]

        total = 0
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                xy = line_intersect(pos[i], dir[i], pos[j], dir[j])
                if xy is not None and np.all(xy[:-1] >= lower_bound) and np.all(xy[:-1] <= upper_bound):
                    total += 1

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 12740
