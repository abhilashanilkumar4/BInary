class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def bfs_traversal(self):
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs_preorder(self, node, result):
        if node:
            result.append(node.value)
            self.dfs_preorder(node.left, result)
            self.dfs_preorder(node.right, result)

    def dfs_inorder(self, node, result):
        if node:
            self.dfs_inorder(node.left, result)
            result.append(node.value)
            self.dfs_inorder(node.right, result)

    def dfs_postorder(self, node, result):
        if node:
            self.dfs_postorder(node.left, result)
            self.dfs_postorder(node.right, result)
            result.append(node.value)

    def dfs_traversal(self, method='preorder'):
        result = []
        if method == 'preorder':
            self.dfs_preorder(self.root, result)
        elif method == 'inorder':
            self.dfs_inorder(self.root, result)
        elif method == 'postorder':
            self.dfs_postorder(self.root, result)
        return result


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("BFS traversal:", tree.bfs_traversal())
print("DFS (preorder) traversal:", tree.dfs_traversal('preorder'))
print("DFS (inorder) traversal:", tree.dfs_traversal('inorder'))
print("DFS (postorder) traversal:", tree.dfs_traversal('postorder'))
