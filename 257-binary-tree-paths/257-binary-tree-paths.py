# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        buf = []
        res = []
        def recurse(node):
            nonlocal buf, res
            if node and not node.left and not node.right:
                buf.append(str(node.val))
                res.append("->".join(buf))
                buf.pop()
                return
            buf.append(str(node.val))
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)
            buf.pop()
            
        recurse(root)
        return res