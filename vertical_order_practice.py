class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def vertical_order_traversal(self, root):
        if root is None: 
            return [] 
        
        #result dict 
        result_dict = {} 

        queue = [(root, 0)] #root, column 

        while queue: 
            node, column = queue.pop(0) 

            if node: 
                if column not in result_dict: 
                    result_dict[column] = [] 
                result_dict[column].append(node.val) 
                queue.append((node.left, column - 1)) 
                queue.append((node.right, column + 1)) 
        
        sorted_dict = sorted(result_dict.keys())
        return [result_dict[col] for col in sorted_dict]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(root.vertical_order_traversal(root))