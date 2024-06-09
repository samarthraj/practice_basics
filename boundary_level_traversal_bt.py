class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def if_leaf_or_not(node):
    return node is not None and node.left is None and node.right is None


def left_boundary(node, result):
    current = node.left

    while current:
        if not if_leaf_or_not(current):
            result.append(current.val)
        if current.left:
            current = current.left
        else:
            current = current.right


def add_leaf_nodes(node, result):
    if node is None:
        return []

    if if_leaf_or_not(node):
        result.append(node.val)
    else:
        add_leaf_nodes(node.left, result)
        add_leaf_nodes(node.right, result)


def right_boundary(node, result):
    current = node.right
    temp = []

    while current:
        if not if_leaf_or_not(current):
            temp.append(current.val)
        if current.right:
            current = current.right
        else:
            current = current.left

    result.extend(temp[::-1])

def boundary_traversal(root):
    result = []
    if root is None:
        return []

    if not if_leaf_or_not(root):
        result.append(root.val)

    left_boundary(root, result)
    add_leaf_nodes(root, result)
    right_boundary(root, result)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)

print(boundary_traversal(root))
