# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        stk = []
        
        ptr = root
        while len(stk) > 0 or ptr != None:
            while ptr != None:
                stk += [ptr]
                ptr = ptr.left
            ptr = stk.pop()
            out += [ptr.val]
            ptr = ptr.right
            
        return out