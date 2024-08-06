class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def leftView(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level_val = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level_val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_val[0])
        return result

    def rightView(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level_val = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level_val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_val[-1])
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(root.leftView(root))
print(root.rightView(root))
