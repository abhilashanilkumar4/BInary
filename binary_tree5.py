class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def is_leaf(self, node):
        return node and not node.left and not node.right

    def sum_of_left_leaves(self, node):
        if not node:
            return 0
        left_sum = 0
        if node.left:
            if self.is_leaf(node.left):
                left_sum += node.left.value
            else:
                left_sum += self.sum_of_left_leaves(node.left)
        if node.right:
            left_sum += self.sum_of_left_leaves(node.right)
        return left_sum

tree = BinaryTree(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)

print("Sum of left leaves:", tree.sum_of_left_leaves(tree.root))
