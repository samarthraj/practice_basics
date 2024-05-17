# representation

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):  # root, left, right
    if root == None:
        return root
    else:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)


def post_order(root):  # left, right, root
    if root == None:
        return root
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=' ')


def in_order(root):  # left root right
    if root == None:
        return root
    else:
        in_order(root.left)
        print(root.val, end=' ')
        in_order(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Preorder Traversal")
preorder(root)
print('\n')

print("Inorder Traversal")
in_order(root)

print('\n')
print("Post-order Traversal")
post_order(root)
