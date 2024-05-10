# Binary Tree Representation
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# root, left, right (where there is root you need to print)
def preorder_traversal(node):
    if node == None:
        return
    else:
        print(node.key, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):  # in means left root right
    if node is None:
        return
    else:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)


def postorder_traversal(node):  # post means left right root
    if node is None:
        return
    else:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Preorder Traversal")
preorder_traversal(root)
print('\n')

print("Inorder Traversal")
inorder_traversal(root)

print('\n')
print("Post-order Traversal")
postorder_traversal(root)
