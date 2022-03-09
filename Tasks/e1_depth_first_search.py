from typing import Hashable, List
import networkx as nx

from collections import deque
import matplotlib.pyplot as plt

# def draw_graph(graph):
#     pos = nx.spring_layout(graph)
#     nx.draw_networkx_nodes(graph, pos)
#     nx.draw_networkx_labels(graph, pos)
#
#     for edge in graph.edges:
#         nx.draw_networkx_edges(
#             graph, pos,
#             edgelist=[(edge[0],edge[1])], connectionstyle="arc3,rad=0.2"
#             )
#
#     plt.show()

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    # # draw_graph(g)
    # path_nodes = []  # порядок обхода узлов
    # # g.nodes  # все узлы
    # # neighbours = g[start_node]  # соседи
    # visited_nodes = {node: False for node in g.nodes}
    # stack = deque()  # стэк из узлов
    # stack.append(start_node)
    # while stack:
    #     current_node = stack.pop()
    #     visited_nodes[current_node] = True
    #     path_nodes.append(current_node)
    #     for neighbour in g[current_node]:
    #         if not visited_nodes[neighbour]:
    #             stack.append(neighbour)
    #
    # print(path_nodes)
    # return path_nodes


# рекурсия:

    visited_nodes = {node: False for node in g.nodes}
    path_nodes = []

    def search(node):
        visited_nodes[node] = True
        path_nodes.append(node)
        for neighbour in g[node]:
            if not visited_nodes[neighbour]:
                search(neighbour)

    search(start_node)

    print(path_nodes)  # проверка
    print(visited_nodes)  # проверка
    return path_nodes


if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    print(dfs(graph, 'A'))