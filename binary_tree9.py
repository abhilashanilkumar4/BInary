class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_level_nodes(root):
    if not root:
        return

    dfs(root, 1)

def dfs(node, level):
    if not node:
        return

    if level % 2 == 1:
        print(node.val)

    dfs(node.left, level + 1)
    dfs(node.right, level + 1)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.right = TreeNode(7)

print("Nodes at odd levels:")
print_odd_level_nodes(root)
