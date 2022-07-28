# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        buf = []
        valid = False
        def bt(node, target):
            nonlocal valid
            if not node.left and not node.right:
                if target == (node.val + sum(buf)):
                    valid = True
                return
            buf.append(node.val)
            if node.left:
                bt(node.left, target)
            if node.right:
                bt(node.right, target)
            buf.pop()
        
        bt(root, targetSum)
        return valid