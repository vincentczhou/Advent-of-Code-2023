class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.status = False

    def accept(self):
        self.status = True

    def reject(self):
        self.status = False

    def xmas(self):
        return self.x + self.m + self.a + self.s

    def get(self, v):
        if v == "x":
            return self.x
        elif v == "m":
            return self.m
        elif v == "a":
            return self.a
        elif v == "s":
            return self.s

    def __repr__(self):
        return f"x:{self.x} m:{self.m} a:{self.a} s:{self.s} status:{self.status}"


def lt(a, b):
    return a < b


def gt(a, b):
    return a > b


def main():
    with open("input") as input:
        wrkflws, parts = input.read().split("\n\n")

        ltgt_dict = {"<": lt, ">": gt}
        wrkflw_dict = {"A": lambda part: part.accept(),
                       "R": lambda part: part.reject()}

        def create_func(s):
            dirs = s.split(",")

            def func(part):
                for dir in dirs:
                    if ":" not in dir:
                        wrkflw_dict[dir](part)
                    else:
                        conditional = dir.split(":")
                        condition = conditional[0]
                        then = conditional[1]
                        v = condition[0]
                        operator = condition[1]
                        n = int(condition[2:])
                        if ltgt_dict[operator](part.get(v), n):
                            wrkflw_dict[then](part)
                            break
            return func

        for wrkflw in wrkflws.split("\n"):
            rules = wrkflw[:-1].split("{")
            wrkflw_dict.update({rules[0]: create_func(rules[1])})

        part_list = []
        for part in parts.split("\n"):
            xmas = []
            for ctgry in part[1:-1].split(","):
                xmas.append(int(ctgry.split("=")[-1]))
            part_list.append(Part(*xmas))

        total = 0
        for part in part_list:
            wrkflw_dict["in"](part)
            if part.status == True:
                total += part.xmas()

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 376008
