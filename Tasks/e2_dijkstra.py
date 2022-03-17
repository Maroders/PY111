from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()



def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    draw_graph(g)
    visited_nodes = []
    final_costs = {node: float("inf") for node in g}
    print(final_costs)
    final_costs[starting_node] = 0
    # visited_nodes.append(starting_node)
    print(final_costs)

    def _way(node):
        if node in visited_nodes:
            return None
        if node not in visited_nodes:
            visited_nodes.append(node)

            for neighbour in g.neighbors(node):
                if neighbour not in visited_nodes:
                    final_costs[neighbour] = g[node][neighbour]["weight"] + final_costs[node]

                print(min(g[node][neighbour]))

            costs = {}
            for neighbour in g.neighbors(node):
                if neighbour not in visited_nodes:
                    costs[neighbour] = g[node][neighbour]["weight"] + final_costs[node]
                    # min_way_node = min(costs, key=costs.get)
            if not costs:
                return None
            else:
                return _way(min(costs, key=costs.get))

    # dict_3 = {'C': 4, 'E': 4}
    # flag = dict_3["C"]
    # list_for_rec = []
    # for i, j in dict_3.items():
    #     if j == flag:
    #         list_for_rec.append(i)

    print(list_for_rec)

    _way(starting_node)
    # print(g["B"]["weight"])
    return final_costs

            # final_costs[neighbour] = min(final_costs[neighbour], g[node][neighbour])
            # print(final_costs)
            #     print(f"{node}-{neighbour}:")
            #     print(g[node][neighbour]["weight"])
            #     print(min(final_costs[neighbour], g[node][neighbour]["weight"]))


if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_nodes_from("ABCDEFG")
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    # sn = "A"
    # print(dijkstra_algo(G, sn))

    sn = "D"
    print(dijkstra_algo(G, sn))