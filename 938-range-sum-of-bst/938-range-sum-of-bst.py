# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.fringe = []
    
    def recurse(self, root, low, high):
        if not root:
            return
        self.recurse(root.left, low, high)
        if root and (root.val >= low) and (root.val <= high):
            self.fringe += [root]
        self.recurse(root.right, low, high)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.fringe = []
        self.recurse(root, low, high)
        
        sum = 0
        for node in self.fringe:
            sum += node.val
        
        return sum