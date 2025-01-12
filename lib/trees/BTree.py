

class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTree:
    def __init__(self, root):
        self.root = root

    def pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)
