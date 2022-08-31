# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getH(node):
            if not node:
                return True, 0
            lS, lH = getH(node.left)
            rS, rH = getH(node.right)
            return lS and rS and abs(lH - rH) <= 1, 1 + max(lH, rH)

        return getH(root)[0]