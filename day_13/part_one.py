def h_sym(section):
    sym_idx = -1
    sym_idxs = []
    for i in range(len(section) - 1):
        if section[i] == section[i + 1]:
            sym_idx = i
            sym_idxs.append(sym_idx)

    final = 0
    for sym_idx in sym_idxs:
        # matches = 0
        valid = False
        limit = min([sym_idx, len(section[sym_idx + 1:]) - 1])
        for t, i in enumerate(range(sym_idx, sym_idx - limit - 1, -1)):
            if section[i] == section[i + (2 * t + 1)]:
                # matches += 1
                valid = True
            else:
                valid = False
                break
        # Assumes only one valid symmetrical line - only valid if it remains symmetrical until secion edge
        if valid:
            final = sym_idx + 1
            break

    return final


def transpose(section):
    transposed = []
    for j in range(len(section[0])):
        col = []
        for i in range(len(section)):
            col.append(section[i][j])
        transposed.append(col)
    return transposed


def print_section(section):
    for line in section:
        print(line)
    print("\n")


def main():
    with open("input") as input:
        sections = []
        for section in input.read().split("\n\n"):
            lines = []
            for line in section.split("\n"):
                lines.append([char for char in line])
            sections.append(lines)

        h_count = 0
        v_count = 0
        for section in sections:
            h = h_sym(section)
            # If a symmetrical line is present (and valid), h_sym will return a value greater than 0
            if h > 0:
                h_count += h
            else:
                v = h_sym(transpose(section))
                v_count += v

        total = v_count + (100 * h_count)

        print(f"The total is: {total}")


if __name__ == "__main__":
    main()

# The total is: 37381
