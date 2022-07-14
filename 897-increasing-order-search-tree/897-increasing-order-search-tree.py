# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy = tx = TreeNode(0, None, None)
        def inorder(node):
            nonlocal tx
            if node:
                inorder(node.left)
                tx.right = TreeNode(node.val, None, None)
                tx = tx.right
                inorder(node.right)
        
        inorder(root)
        return dummy.right