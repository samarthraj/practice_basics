class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rightView(self, root): 
        #do bfs 
        queue = [root] 
        result_list = []

        while queue: 
            queue_length = len(queue)
            level_wise = [] 

            for k in range(queue_length):
                node = queue.pop(0)  
                level_wise.append(node.val) 
            
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right) 
            result_list.append(level_wise[-1])
        return result_list

    def topView(self, root):

        #define a dictionary which stores the coordinates 
        dict = {} 
        queue = [(root, 0)] #root and the column no 

        if root is None:
            return []

        while queue: 
            for k in range(len(queue)): 
                node, col = queue.pop(0)  
                if col not in dict: 
                    dict[col] = [] 
                dict[col].append(node.val) 

                if node.left: 
                    queue.append((node.left, col - 1)) 
                if node.right: 
                    queue.append((node.right, col + 1)) 
        sorted_dict = sorted(dict.keys()) 
        return [dict[col][-1] for col in sorted_dict]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

#print(root.rightView(root))
print(root.topView(root)) 
    