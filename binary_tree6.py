class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PerfectBinaryTree:
    def __init__(self, depth):
        self.root = self._create_perfect_binary_tree(depth)

    def _create_perfect_binary_tree(self, depth, value=1):
        if depth == 0:
            return None
        node = Node(value)
        node.left = self._create_perfect_binary_tree(depth-1, value*2)
        node.right = self._create_perfect_binary_tree(depth-1, value*2+1)
        return node

    def sum_of_all_nodes(self, node):
        if not node:
            return 0
        return node.value + self.sum_of_all_nodes(node.left) + self.sum_of_all_nodes(node.right)


tree = PerfectBinaryTree(3)
print("Sum of all nodes:", tree.sum_of_all_nodes(tree.root))
