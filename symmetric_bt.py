class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def symmetric_bt(root): 

    if root is None:
        return False 
    
    #use pre order 
    print(root.val, end = ' ')
    symmetric_bt(root.left) 
    symmetric_bt(root.right) 
     
    

