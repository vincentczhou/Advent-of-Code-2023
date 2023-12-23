import numpy as np


class Brick:
    def __init__(self, xo, yo, zo, xi, yi, zi):
        self.xo = int(xo)
        self.yo = int(yo)
        self.zo = int(zo)
        self.xi = int(xi)
        self.yi = int(yi)
        self.zi = int(zi)

        self.parents = []
        self.children = []

    def z_min(self):
        return min(self.zo, self.zi)

    def z_max(self):
        return max(self.zo, self.zi)

    def add_parent(self, p_bricks):
        self.parents += p_bricks

    def add_children(self, c_bricks):
        self.children.append(c_bricks)

    # def o(self):
    #     return np.array([self.xo, self.yo, self.zo])

    # def i(self):
    #     return np.array([self.xi, self.yi, self.zi])

    # def vector(self):
    #     return self.i() - self.o()

    # @staticmethod
    # def point_intersect(bo, bi):
    #     return np.all(bo.o() == bi.o() and bo.i() == bi.i())

    # @staticmethod
    # def line_intersect(bo, bi):
    #     r = bo.vector()
    #     s = bi.vector()
    #     q = np.array([bo.xo - bi.xo, bo.yo -
    #                  bi.yo, bo.zo - bi.zo])

    #     dotqr = np.dot(q, r)
    #     dotqs = np.dot(q, s)
    #     dotrs = np.dot(r, s)
    #     dotrr = np.dot(r, r)
    #     dotss = np.dot(s, s)

    #     denom = dotrr * dotss - dotrs * dotrs
    #     num = dotqs * dotrs - dotqr * dotss

    #     t = num / denom
    #     u = (dotqs + t * dotrs) / dotss

    #     po = bo.o() + t * r
    #     pi = bi.o() + u * s

    #     return (0 <= t and t <= 1 and 0 <= u and u <= 1) and (np.linalg.norm(pi - po) == 0)

    # @staticmethod
    # def pl_intersect(bo, bi):
    #     v = bi.vector()
    #     pq = bo.o() - bi.o()
    #     d = np.linalg.norm(np.cross(v, pq)) / np.linalg.norm(v)
    #     return d == 0

    # @staticmethod
    # def intersect(bo, bi, t=False):
    #     if t:
    #         bo = bo.copy_top()
    #     r = bo.vector()
    #     s = bi.vector()
    #     intersect = False
    #     if not np.all(r == 0) and not np.all(s == 0):
    #         intersect = Brick.line_intersect(bo, bi)
    #     elif np.all(r == 0) and np.all(s == 0):
    #         intersect = Brick.point_intersect(bo, bi)
    #     elif np.all(r == 0) and not np.all(s == 0):
    #         intersect = Brick.pl_intersect(bo, bi)
    #     elif not np.all(r == 0) and np.all(s == 0):
    #         intersect = Brick.pl_intersect(bi, bo)
    #     return intersect

    # def copy_top(self):
    #     return Brick(self.xo, self.yo, self.zo + 1, self.xi, self.yi, self.zi + 1)

    # def __eq__(self, other):
    #     return (self.z_min() == other.z_min())

    def __lt__(self, other):
        return (self.z_min() < other.z_min())

    def __gt__(self, other):
        return (self.z_min() > other.z_min())

    def __le__(self, other):
        return (self.z_min() < other.z_min()) or (self.z_min() == other.z_min())

    def __ge__(self, other):
        return (self.z_min() > other.z_min()) or (self.z_min() == other.z_min())

    def __repr__(self):
        return f"({self.xo}, {self.yo}, {self.zo})-({self.xi}, {self.yi}, {self.zi})"


def main():
    with open("input") as input:
        bricks = []
        for line in input.read().split("\n"):
            o, i = line.split("~")
            bricks.append(Brick(*(o.split(",") + i.split(","))))

        bricks.sort()

        x_min = None
        x_max = None
        y_min = None
        y_max = None
        for brick in bricks:
            cx_min = min(brick.xo, brick.xi)
            cx_max = max(brick.xo, brick.xi)
            cy_min = min(brick.yo, brick.yi)
            cy_max = max(brick.yo, brick.yi)
            if x_min == None or x_max == None or y_min == None or y_max == None:
                x_min = cx_min
                x_max = cx_max
                y_min = cy_min
                y_max = cy_max
            elif cx_min < x_min:
                x_min = cx_min
            elif cx_max > x_max:
                x_max = cx_max
            elif cy_min < y_min:
                y_min = cy_min
            elif cy_max > y_max:
                y_max = cy_max

        assert x_min == 0 and x_max >= 0 and y_min == 0 and y_max >= 0
        floor = Brick(x_min, y_min, 0, x_max, y_max, 0)
        gravity = [[floor for y in range(y_min, y_max + 1)]
                   for x in range(x_min, x_max + 1)]

        for brick in bricks:
            cx_min = min(brick.xo, brick.xi)
            cx_max = max(brick.xo, brick.xi)
            cy_min = min(brick.yo, brick.yi)
            cy_max = max(brick.yo, brick.yi)
            parents = [gravity[cx_min][cy_min]]
            if cx_min != cx_max and cy_min == cy_max:
                for x in range(cx_min, cx_max + 1):
                    curr = gravity[x][cy_min]
                    if curr.z_max() > parents[0].z_max():
                        parents = [curr]
                    elif curr.z_max() == parents[0].z_max() and curr not in parents:
                        parents.append(curr)
                    gravity[x][cy_min] = brick
            elif cy_min != cy_max and cx_min == cx_max:
                for y in range(cy_min, cy_max + 1):
                    curr = gravity[cx_min][y]
                    if curr.z_max() > parents[0].z_max():
                        parents = [curr]
                    elif curr.z_max() == parents[0].z_max() and curr not in parents:
                        parents.append(curr)
                    gravity[cx_min][y] = brick
            elif cx_min == cx_max and cy_min == cy_max:
                gravity[cx_min][cy_min] = brick
            brick.add_parent(parents)
            fall_dist = brick.z_min() - parents[0].z_max() - 1
            brick.zo = brick.zo - fall_dist
            brick.zi = brick.zi - fall_dist
            for parent in parents:
                parent.add_children(brick)

        total = 0
        for brick in bricks:
            removable = True
            for child in brick.children:
                if len(child.parents) < 2:
                    removable = False
                    break
            if removable:
                total += 1

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 411
