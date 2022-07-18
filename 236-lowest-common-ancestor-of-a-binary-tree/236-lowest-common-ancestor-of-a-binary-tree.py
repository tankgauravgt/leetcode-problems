# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            ls = lca(node.left, p, q)
            rs = lca(node.right, p, q)
            if ls and rs:
                return node
            if ls:
                return ls
            if rs:
                return rs
            return None
        
        return lca(root, p, q)