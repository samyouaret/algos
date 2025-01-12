

class BSTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return BSTreeNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def delete(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # case 1 no children
            if root.right is None and root.left is None:
                return None
            # case 2 one child
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            # case 3 two children
            # find the smallest value in the right subtree
            min_node = self.find_min(root.right)
            # copy min value to that node
            root.value = min_node.value
            # delete the min value node (reduced to case 1)
            root.right = self.delete(root.right, min_node.value)

        return root

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def pre_order(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.value, end=' ')
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=' ')

    def height(self, node):
        # Base case: if the node is None, the height is -1
        if node is None:
            return -1  # or return 0 based on convention

        # Recursively find the height of left and right subtrees
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # The height of the tree is the max height of the two subtrees + 1
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    tree = BSTree()
    tree.root = tree.insert(tree.root, 5)
    tree.root = tree.insert(tree.root, 3)
    tree.root = tree.insert(tree.root, 7)
    tree.root = tree.insert(tree.root, 2)
    tree.root = tree.insert(tree.root, 4)
    tree.root = tree.insert(tree.root, 6)
    tree.root = tree.insert(tree.root, 8)

    print("Pre-order traversal:")
    tree.pre_order(tree.root)
    print("\nIn-order traversal:")
    tree.in_order(tree.root)
    print("\nPost-order traversal:")
    tree.post_order(tree.root)

    print("\nHeight of the tree:", tree.height(tree.root))

    print("\nDeleting node with value 3:")
    tree.root = tree.delete(tree.root, 3)
    print("In-order traversal after deletion:")
    tree.in_order(tree.root)
    print("\nHeight of the tree after deletion:", tree.height(tree.root))