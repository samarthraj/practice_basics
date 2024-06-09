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
    left_to_right = True

    while queue:
        length_of_queue = len(queue)
        level_res = []

        for _ in range(length_of_queue):
            node = queue.pop(0)

            if left_to_right is True:
                level_res.append(node.val)
            else:
                level_res.insert(0, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_res)
        left_to_right = not left_to_right
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform level order traversal and print the result
print(level_order_traversal(root))
