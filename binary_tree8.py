class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    level_sum = root.val
    max_sum = root.val
    q = [root]

    while q:
        level_size = len(q)
        level_sum = 0

        for _ in range(level_size):
            node = q.pop(0)
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum

    return max_sum
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.right = TreeNode(7)

max_sum = max_level_sum(root)
print(f"Maximum level sum: {max_sum}")  
