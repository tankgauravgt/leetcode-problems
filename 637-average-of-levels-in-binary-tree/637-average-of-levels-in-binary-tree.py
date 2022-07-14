from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        fringe = deque([root])
        
        out = []
        while fringe:
            N = len(fringe)
            s = 0
            count = 0
            for ix in range(N):
                node = fringe.popleft()
                if node:
                    count += 1
                    s += node.val
                    fringe.append(node.left)
                    fringe.append(node.right)
            if count > 0:
                out.append(s / count)
        
        return out