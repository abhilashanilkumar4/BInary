class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, AB):
        if AB == "LEFT_no":
            return self.LEFT(tree.root, "")
        elif AB == "CENTRE_no":
            return self.CENTRE(tree.root, "")
        elif AB == "RIGHT_no":
            return self.RIGHT(tree.root, "")
        else:
            print("AB " + str(AB) + " is not supported.")
            return False

    def LEFT(self, start, CD):
        if start:
            CD += (str(start.value) + "-")
            CD = self.LEFT(start.left, CD)
            CD = self.LEFT(start.right, CD)
        return CD

    def CENTRE(self, start, CD):
        if start:
            CD = self.CENTRE(start.left, CD)
            CD += (str(start.value) + "-")
            CD = self.CENTRE(start.right, CD)
        return CD

    def RIGHT(self, start, CD):
        if start:
            CD = self.RIGHT(start.left, CD)
            CD = self.RIGHT(start.right, CD)
            CD += (str(start.value) + "-")
        return CD


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("LEFT numbers: " + tree.print_tree("LEFT_no"))
print("centre numbers: " + tree.print_tree("CENTRE_no"))
print("right numbers: " + tree.print_tree("RIGHT_no"))
