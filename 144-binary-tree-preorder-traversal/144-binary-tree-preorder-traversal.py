# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        stk = [root]
        
        while len(stk) > 0:
            ptr = stk.pop()
            if ptr != None:
                out = out + [ptr.val]
                if ptr.right != None:
                    stk += [ptr.right]
                if ptr.left != None:
                    stk += [ptr.left]
        
        return out