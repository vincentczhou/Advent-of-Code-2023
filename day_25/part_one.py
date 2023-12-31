import networkx as nx


def main():
    with open("input") as input:
        G = nx.Graph()
        for line in input.read().split("\n"):
            c, cns = line.split(":")
            for cn in cns.strip().split(" "):
                G.add_edge(c, cn)

        cuts = nx.minimum_edge_cut(G)
        G.remove_edges_from(cuts)
        a, b = next(iter(cuts))
        a_len = len(nx.bfs_tree(G, a).nodes)
        b_len = len(nx.bfs_tree(G, b).nodes)

        print(f"The total is: {a_len * b_len}")


if __name__ == "__main__":
    main()

# The total is: 598120
