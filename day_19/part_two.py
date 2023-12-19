class Part:
    def __init__(self, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max):
        self.x_max = x_max
        self.m_max = m_max
        self.a_max = a_max
        self.s_max = s_max
        self.x_min = x_min
        self.m_min = m_min
        self.a_min = a_min
        self.s_min = s_min

    def accept(self, obj):
        obj[0] += (self.x_max - self.x_min) * (self.m_max - self.m_min) * \
            (self.a_max - self.a_min) * (self.s_max - self.s_min)

    def reject(self, obj):
        obj[0] += 0

    def set_max(self, v, n):
        if v == "x":
            self.x_max = n
        elif v == "m":
            self.m_max = n
        elif v == "a":
            self.a_max = n
        elif v == "s":
            self.s_max = n

    def set_min(self, v, n):
        if v == "x":
            self.x_min = n
        elif v == "m":
            self.m_min = n
        elif v == "a":
            self.a_min = n
        elif v == "s":
            self.s_min = n

    def copy(self):
        return Part(self.x_min, self.x_max, self.m_min, self.m_max, self.a_min, self.a_max, self.s_min, self.s_max)

    def __repr__(self):
        return f"x:{(self.x_min, self.x_max)} m:{(self.m_min, self.m_max)} a:{(self.a_min, self.a_max)} s:{(self.s_min, self.s_max)}"


def main():
    with open("input") as input:
        wrkflws, parts = input.read().split("\n\n")

        total = [0]

        op_dict = {"<": lambda part, v, n: part.set_max(
            v, n), ">": lambda part, v, n: part.set_min(v, n + 1)}
        opc_dict = {"<": lambda part, v, n: part.set_min(
            v, n), ">": lambda part, v, n: part.set_max(v, n + 1)}
        wrkflw_dict = {"A": lambda part: part.accept(total),
                       "R": lambda part: part.reject(total)}

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
                        new_part = part.copy()
                        op_dict[operator](new_part, v, n)
                        wrkflw_dict[then](new_part)
                        opc_dict[operator](part, v, n)
            return func

        for wrkflw in wrkflws.split("\n"):
            rules = wrkflw[:-1].split("{")
            wrkflw_dict.update({rules[0]: create_func(rules[1])})

        part = Part(1, 4001, 1, 4001, 1, 4001, 1, 4001)
        wrkflw_dict["in"](part)

        print(f"The total is: {total[0]}")


if __name__ == "__main__":
    main()

# The total is: 124078207789312
