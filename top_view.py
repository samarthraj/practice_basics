class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def topView(root):
    if root is None:
        return []

    result_dict = {}
    queue = [(root, 0)]

    while queue:
        node, column = queue.pop(0)
        if node:
            if column not in result_dict:
                result_dict[column] = node.val
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    sorted_keys = sorted(result_dict.keys())
    return [result_dict[col] for col in sorted_keys]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(topView(root))
