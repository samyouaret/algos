
from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return
        raise Exception("Vertex already exists")

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            raise KeyError("Vertex does not exist")
            return
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            raise KeyError("Vertex does not exist")
        self.adj_list[vertex1].remove(vertex2)
        self.adj_list[vertex2].remove(vertex1)

    def display(self):
        """Display the adjacency list of the graph."""
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    def bfs(self, start_vertex):
        """Perform BFS traversal starting from start_vertex."""
        visited = set()  # Track visited vertices
        queue = deque([start_vertex])  # Initialize the queue
        result = []  # To store the traversal order

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                result.append(current)

                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def dfs_recursive(self, vertex, visited=None, result=None):
        """Perform DFS traversal using recursion."""
        if visited is None:
            visited = set()
        if result is None:
            result = []

        visited.add(vertex)
        result.append(vertex)

        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)

        return result
