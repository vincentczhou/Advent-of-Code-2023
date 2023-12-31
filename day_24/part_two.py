import sympy


def main():
    with open("input") as input:
        pos = []
        dir = []
        for line in input.read().split("\n"):
            p, d = line.split("@")
            pos.append(tuple([int(x) for x in p.split(",")]))
            dir.append(tuple([int(x) for x in d.split(",")]))

        # https://youtu.be/guOyA7Ijqgk?si=-7aTd1Vtz0Wt_3KI
        x, y, z, vx, vy, vz = sympy.symbols("x y z vx vy vz")
        equations = []
        for i in range(len(pos)):
            hx, hy, hz = pos[i]
            hvx, hvy, hvz = dir[i]
            equations.append((x - hx) * (hvy - vy) - (y - hy) * (hvx - vx))
            equations.append((y - hy) * (hvz - vz) - (z - hz) * (hvy - vy))
        answers = sympy.solve(equations)[0]

        print(f"The total is: {answers[x] + answers[y] + answers[z]}")


if __name__ == "__main__":
    main()

# The total is: 741991571910536
