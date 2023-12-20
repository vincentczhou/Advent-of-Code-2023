class Module:
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest
        self.mod = "Module"

    def __repr__(self):
        return f"mod: {self.mod} name: {self.name} dest: {self.dest} "


class Button(Module):
    def __init__(self):
        super().__init__("button", ["broadcaster"])
        self.mod = "Button"

    def send(self):
        return [(self.name, d, "low") for d in self.dest]


class Broadcaster(Module):
    def __init__(self, name, dest):
        super().__init__(name, dest)
        self.mod = "Broadcaster"
        self.t = "low"

    def recv(self, t, n):
        self.t = t
        return self.send()

    def send(self):
        return [(self.name, d, self.t) for d in self.dest]


class FF(Module):
    def __init__(self, name, dest):
        self.status = False
        super().__init__(name, dest)
        self.mod = "FF"

    def recv(self, t, n):
        if t == "low":
            self.status = not self.status
            return self.send()
        else:
            return None

    def send(self):
        t = "high" if self.status else "low"
        return [(self.name, d, t) for d in self.dest]

    def __repr__(self):
        return super().__repr__() + f"status: {self.status} "


class Conjunction(Module):
    def __init__(self, name, dest, src):
        super().__init__(name, dest)
        self.mod = "Conjunction"
        self.src = src
        self.status = {s: "low" for s in src}

    def recv(self, t, n):
        self.status[n] = t
        return self.send()

    def send(self):
        t = "low" if all(x == "high" for x in self.status.values()) else "high"
        return [(self.name, d, t) for d in self.dest]

    def __repr__(self):
        return super().__repr__() + f"src: {self.src} "


def main():
    with open("input") as input:
        modules = {}
        cnj = {}
        for line in input.read().split("\n"):
            m, d = line.split(" -> ")
            if m == "broadcaster":
                modules.update({m: Broadcaster(m, d.split(", "))})
            elif m[0] == "%":
                modules.update({m[1:]: FF(m[1:], d.split(", "))})
            elif m[0] == "&":
                cnj.update({m[1:]: [d.split(", "), []]})

        for m in modules.items():
            name, obj = m
            for d in obj.dest:
                if d in cnj.keys():
                    cnj[d][1].append(name)
        for c in cnj.items():
            name, ds = c
            obj_dest = ds[0]
            for d in obj_dest:
                if d in cnj.keys():
                    cnj[d][1].append(name)

        for c in cnj.items():
            name, ds = c
            modules.update({name: Conjunction(name, *ds)})

        low = 0
        high = 0
        queue = []

        for i in range(1000):
            queue.append(Button().send())
            while len(queue) != 0:
                send_sigs = queue.pop(0)
                for send_sig in send_sigs:
                    s, d, t = send_sig
                    if t == "low":
                        low += 1
                    elif t == 'high':
                        high += 1
                    send = None
                    if d in modules.keys():
                        send = modules[d].recv(t, s)
                    if send is not None:
                        queue.append(modules[d].send())

        print(f"The total is: {low * high}")


if __name__ == "__main__":
    main()

# The total is: 832957356
