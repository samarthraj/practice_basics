class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self, node):
        return node is not None and node.left is None and node.right is None

    def left_boundary(self, node, result):
        current = node.left

        while current:
            if not self.is_leaf(current):
                result.append(current.val)

            if current.left:
                current = current.left
            else:
                current = current.right

    def add_leaf_node(self, node, result):
        if root is None:
            return []

        if self.is_leaf(node):
            result.append(node.val)
        else:
            self.add_leaf_node(node.left, result)
            self.add_leaf_node(node.right, result)

    def right_boundary(self, node, result):
        current = node.right
        temp = []

        while current:
            if not self.is_leaf(current):
                temp.append(current.val)

            if current.right:
                current = current.right
            else:
                current = current.left

        result.extend(temp[::-1])

    def boundary_traversal(self, root):
        result = []

        if root is None:
            return []

        if not self.is_leaf(root):
            result.append(root.val)

        self.left_boundary(root, result)
        self.add_leaf_node(root, result)
        self.right_boundary(root, result)

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

print(root.boundary_traversal(root))
# Output: [1, 2, 4, 8, 9, 6, 7, 3]
