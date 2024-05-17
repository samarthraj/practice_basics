class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        levels = []
        for _ in range(0, len(queue)):
            node = queue.pop(0)
            levels.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(levels)

    return result


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# Perform level order traversal and print the result
print(level_order_traversal(root))  # Output: [[1], [2, 3], [4, 5]]
