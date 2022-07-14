# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        memo = {}
        found = False
        def search(node):
            nonlocal memo, found
            if node:
                if (k - node.val) not in memo:
                    memo.update({node.val: node})
                    search(node.left)
                    search(node.right)
                else:
                    found = True
        
        search(root)
        return found