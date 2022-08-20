# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def solve(node):
            if not node:
                return None
            
            ltree = node.left
            rtree = node.right
            
            node.left = None
            node.right = None
            
            node.right = solve(ltree)
            
            temp = node
            while temp and temp.right:
                temp = temp.right
                
            temp.right = solve(rtree)
            
            return node
        
        solve(root)