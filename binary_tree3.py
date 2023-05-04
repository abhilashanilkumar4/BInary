class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.value, end=' ')
    print_leaves(node.left)
    print_leaves(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Leaves of the tree are:", end=' ')
print_leaves(root)
