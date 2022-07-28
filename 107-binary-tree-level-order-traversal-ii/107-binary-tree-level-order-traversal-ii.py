from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        fringe = deque([root])
        
        res = []
        while fringe:
            L = len(fringe)
            tarr = []
            for ix in range(L):
                node = fringe.popleft()
                if node:
                    tarr.append(node.val)
                    fringe.append(node.left)
                    fringe.append(node.right)
            if tarr:
                res.append(tarr)
        
        return res[::-1]