# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        valid = True
        def dfs(node):
            nonlocal valid
            if not node:
                return 0
            lx = 0
            rx = 0
            lx = dfs(node.left)
            rx = dfs(node.right)
            if abs(lx - rx) > 1:
                valid = False
            return 1 + max(lx, rx)
                
        dfs(root)
        return valid