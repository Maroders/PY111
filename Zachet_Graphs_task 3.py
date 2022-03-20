from collections import deque
import networkx as nx
from matplotlib import pyplot as plt
from typing import Hashable, List


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0],edge[1])], connectionstyle="arc3,rad=0.2"
            )

    plt.show()

def dfs(g: nx.Graph, start_node: Hashable) -> int:
    stack = deque()
    stack.append(start_node)
    visited_nodes = {node: False for node in g}
    connectivity = 0

    while True:
        connectivity += 1
        while stack:
            next_node = stack.pop()
            visited_nodes[next_node] = True
            for neighbor in g.neighbors(next_node):
                if not visited_nodes[neighbor] and neighbor not in stack:
                    stack.append(neighbor)
        if all(list(visited_nodes.values())):
            return connectivity
        else:
            for node in visited_nodes:
                if not visited_nodes[node]:
                    stack.append(node)
                    break


if __name__ == '__main__':
    graph = nx.Graph()

    graph.add_nodes_from("ABCDEFGJHKLM")
    graph.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "E"),
        ("E", "F"),
        ("B", "E"),
        ("C", "D"),
        ("D", "E"),
        ("B", "D"),
        ("G", "D"),
        ("D", "A"),
        ("H", "K"),
        ("K", "L"),
        ("K", "M"),
    ])

    # draw_graph(graph)
    print(dfs(graph, "A"))

