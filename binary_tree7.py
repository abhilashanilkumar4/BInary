class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, x):
    count = [0] 

    def dfs(node):
        if not node:
            return 0

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        total_sum = node.val + left_sum + right_sum

        if total_sum == x:
            count[0] += 1

        return total_sum

    dfs(root)
    return count[0]


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

x = 22
count = count_subtrees_with_sum(root, x)
print(f"Number of subtrees with sum {x}: {count}")
