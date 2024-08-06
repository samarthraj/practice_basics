class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def vertical_order_traversal(self, root): 

        result_dict = {} 
        queue = [(root, 0)] #root, col numb 

        if root is None:
            return []

        while queue: 
            node, col = queue.pop(0)

            if node: 
                if col not in result_dict: 
                    result_dict[col] = [] 
                result_dict[col].append(node.val) 

                if node.left: 
                    queue.append((node.left, col - 1)) 
                if node.right: 
                    queue.append((node.right, col + 1)) 
            
        #print(result_dict)
        sorted_keys = sorted(result_dict.keys()) 
        return [result_dict[c] for c in sorted_keys]



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(root.vertical_order_traversal(root))