class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.height_of_bt(root) != -1:
            return True 
        return False 

    def height_of_bt(self, root): 
        if root is None:
            return 0 
        left_ht = self.height_of_bt(root.left) 
        if left_ht == -1: 
            return -1
        right_ht = self.height_of_bt(root.right) 
        if right_ht == -1: 
            return -1 
        
        if abs(left_ht - right_ht) > 1: 
            return -1 
        return 1 + max(left_ht, right_ht) 




