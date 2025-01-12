import unittest
from lib.trees.BSTree import BSTree


class TestBSTree(unittest.TestCase):
    def setUp(self):
        """Set up a sample BSTree for testing."""
        #        20
        #       /  \
        #     10    30
        #    /  \   /  \
        #   5   15 25   35
        self.tree = BSTree()
        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.tree.root = self.tree.insert(self.tree.root, value)

    def test_insert(self):
        """Test insertion into the BST."""
        # Insert a new value
        self.tree.insert(self.tree.root, 40)
        self.assertEqual(self.tree.root.right.right.right.value, 40)
        # Insert a duplicate value (should still maintain structure)
        self.tree.insert(self.tree.root, 30)
        self.assertEqual(self.tree.root.right.value, 30)

    def test_find_min(self):
        """Test finding the minimum value in the BST."""
        min_node = self.tree.find_min(self.tree.root)
        self.assertEqual(min_node.value, 5)

    def test_delete_leaf_node(self):
        """Test deleting a leaf node."""
        self.tree.delete(self.tree.root, 5)
        self.assertIsNone(self.tree.root.left.left)  # 5 was a leaf

    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child."""
        self.tree.delete(self.tree.root, 15)
        self.assertIsNone(self.tree.root.left.right)  # 15 was removed

    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children."""
        self.tree.delete(self.tree.root, 20)  # Root node
        # Root should have been replaced
        self.assertNotEqual(self.tree.root.value, 20)
        min_node = self.tree.find_min(self.tree.root.right)
        # New root shouldn't be the min
        self.assertNotEqual(min_node.value, self.tree.root.value)

    def test_height(self):
        """Test height calculation."""
        # Height of the tree with values
        self.assertEqual(self.tree.height(self.tree.root), 2)
        self.tree.root = None
        # Empty tree height
        self.assertEqual(self.tree.height(self.tree.root), -1)

    def test_traversals(self):
        """Test preorder, inorder, and postorder traversals."""
        expected_preorder = [20, 10, 5, 15, 30, 25, 35]
        expected_inorder = [5, 10, 15, 20, 25, 30, 35]
        expected_postorder = [5, 15, 10, 25, 35, 30, 20]

        # Collect traversal outputs
        result_preorder = []
        result_inorder = []
        result_postorder = []

        def collect_preorder(node):
            if node:
                result_preorder.append(node.value)
                collect_preorder(node.left)
                collect_preorder(node.right)

        def collect_inorder(node):
            if node:
                collect_inorder(node.left)
                result_inorder.append(node.value)
                collect_inorder(node.right)

        def collect_postorder(node):
            if node:
                collect_postorder(node.left)
                collect_postorder(node.right)
                result_postorder.append(node.value)

        collect_preorder(self.tree.root)
        collect_inorder(self.tree.root)
        collect_postorder(self.tree.root)

        self.assertEqual(result_preorder, expected_preorder)
        self.assertEqual(result_inorder, expected_inorder)
        self.assertEqual(result_postorder, expected_postorder)