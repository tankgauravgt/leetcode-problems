# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node:
                if node.left and node.right:
                    return 1 + min(dfs(node.left), dfs(node.right))
                if node.left:
                    return 1 + dfs(node.left)
                if node.right:
                    return 1 + dfs(node.right)
                if not node.left and not node.right:
                    return 1
            return 0
        
        return dfs(root)