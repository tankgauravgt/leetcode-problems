# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def dfs(node, cmax):
            nonlocal count
            if node:
                if node.val >= cmax:
                    count += 1
                cmax = max(node.val, cmax)
                dfs(node.left, cmax)
                dfs(node.right, cmax)
        
        dfs(root, -(10 ** 5))
        return count