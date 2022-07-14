# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            nonlocal seq
            if node and not node.left and not node.right:
                seq.append(node.val)
            if node and node.left:
                dfs(node.left)
            if node and node.right:
                dfs(node.right)

        seq = []
        dfs(root1)
        s1 = seq.copy()
        
        seq = []
        dfs(root2)
        s2 = seq.copy()
        
        return s1 == s2