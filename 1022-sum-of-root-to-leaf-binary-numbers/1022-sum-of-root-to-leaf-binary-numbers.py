# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        path = []
        count = 0
        def dfs(node):
            nonlocal path, count
            if node:
                if not node.left and not node.right:
                    path.append(node.val)
                    count += int("".join(list(map(str, path))), 2)
                    path.pop()
                    
                if node.left:
                    path.append(node.val)
                    dfs(node.left)
                    path.pop()
                if node.right:
                    path.append(node.val)
                    dfs(node.right)
                    path.pop()
        
        dfs(root)
        return count