class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root):
    if root is None:
        return []

    result_arr = []
    queue = [root]

    while queue:
        len_of_queue = len(queue)
        each_level_val = []

        for _ in range(len_of_queue):
            node = queue.pop(0)
            each_level_val.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result_arr.append(each_level_val)

    return [val[0] for val in result_arr]
# 1,2,4


def right_view(root):
    if root is None:
        return []

    result_arr = []
    queue = [root]

    while queue:
        len_of_queue = len(queue)
        each_level_val = []

        for _ in range(len_of_queue):
            node = queue.pop(0)
            each_level_val.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result_arr.append(each_level_val)

    return [val[-1] for val in result_arr]
# 1,3,7


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(left_view(root))
print(right_view(root))
