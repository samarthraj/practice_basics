# Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def preorder_traversal(node):  # root, left, right
    if node is None:
        return
    else:
        print(node.key, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder_traversal(root)
