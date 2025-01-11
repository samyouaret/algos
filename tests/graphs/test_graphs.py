import unittest
from lib.graphs.Graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        """Initialize a graph instance before each test."""
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(4, 5)

    def test_add_vertex(self):
        """Test adding a vertex."""
        self.graph.add_vertex(6)
        self.assertIn(6, self.graph.adj_list)
        self.assertEqual(self.graph.adj_list[6], [])

    def test_add_edge(self):
        """Test adding edges."""
        self.graph.add_vertex(6)
        self.graph.add_edge(5, 6)
        self.assertIn(6, self.graph.adj_list[5])
        self.assertIn(5, self.graph.adj_list[6])  # Undirected edge
        # 5 now has two neighbors
        self.assertEqual(len(self.graph.adj_list[5]), 2)

    def test_delete_edge(self):
        """Test deleting edges."""
        self.graph.delete_edge(3, 4)
        self.assertNotIn(4, self.graph.adj_list[3])
        self.assertNotIn(3, self.graph.adj_list[4])  # Undirected edge

        self.graph.delete_edge(1, 2)
        self.assertNotIn(2, self.graph.adj_list[1])
        self.assertNotIn(1, self.graph.adj_list[2])

    def test_bfs(self):
        """Test BFS traversal."""
        # BFS starting from vertex 1
        bfs_result = self.graph.bfs(1)
        self.assertEqual(bfs_result, [1, 2, 3, 4, 5])

        # BFS starting from vertex 3
        bfs_result = self.graph.bfs(3)
        self.assertEqual(bfs_result, [3, 1, 4, 2, 5])

    def test_dfs(self):
        """Test DFS traversal."""
        # DFS starting from vertex 1
        dfs_result = self.graph.dfs_recursive(1)
        self.assertEqual(dfs_result, [1, 2, 4, 3, 5])

        # DFS starting from vertex 3
        dfs_result = self.graph.dfs_recursive(3)
        self.assertEqual(dfs_result, [3, 1, 2, 4, 5])


if __name__ == "__main__":
    unittest.main()
