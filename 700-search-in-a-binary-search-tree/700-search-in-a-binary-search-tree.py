# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        tree = None
        def search(node, val):
            nonlocal tree
            if node:
                if node.val == val:
                    tree = node
                    return
                if node.val > val:
                    search(node.left, val)
                    return
                if node.val < val:
                    search(node.right, val)
                    return
        
        search(root, val)
        return tree