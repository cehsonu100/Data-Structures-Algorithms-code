""""
use adjacency list to represent the graph
e.g.
(a)-(c)
(b)-(c)-(e)
(c)-(b)-(e)
(d)-(c)
(e)-(c)
(f)
above: first element in array is vertex then defines the edges from the vertex of value first element
"""

from _collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.set_of_edges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        edges = (u, v)
        self.set_of_edges.append(edges)  # adding this to use in draw_graph() method

    def get_edges(self):
        # edges will be only having two vertices
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges

    def draw_graph(self):
        G = nx.Graph()
        G.add_edges_from(self.set_of_edges)
        nx.draw(G, with_labels=True)
        plt.savefig("graph.png")  # save as png
        plt.show()  # display


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('Bangalore', 'Hyderabad')
    graph.add_edge('Bangalore', 'New York')
    graph.add_edge('Delhi', 'Kota')
    graph.add_edge('Hyderabad', 'Goa')
    graph.add_edge('J&K', 'UK')
    graph.add_edge('UK', 'Norway')
    graph.add_edge('Kota', 'Ahamadabad')
    graph.add_edge('New York', 'Silicon Valley')
    graph.add_edge('New York', 'Canada')
    graph.add_edge('Times Square', 'Time Square')
    print(graph.graph)
    graph.draw_graph()
    # print(graph.get_edges())
