from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two nodes in the graph.
        """
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        if self.graph:
            for vertex in self.graph:
                print(f"{vertex}: {self.graph[vertex]}")




graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

graph.add_edge('A','B')
graph.add_edge('B','C')

graph.display()
        