# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def rec(r1, r2):
            if not r1 and not r2:
                return True
            elif (r1 and not r2) or (r2 and not r1):
                return False
            else:
                if r1.val != r2.val:
                    return False
                lval = rec(r1.left, r2.right)
                rval = rec(r1.right, r2.left)
                return True and lval and rval
        
        return rec(root, root)