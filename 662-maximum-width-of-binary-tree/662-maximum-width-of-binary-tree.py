from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        buf = deque()
        buf.append((root, 0, 1))
        
        res = 0
        while buf:
            n = len(buf)
            _max = 0
            _min = float('inf')
            for ix in range(n):
                node = buf.popleft()
                if node[0]:
                    buf.append((node[0].left, 2 * node[1] + 1, node[2] + 1))
                    buf.append((node[0].right, 2 * node[1] + 2, node[2] + 1))
                    _min = min(_min, node[1])
                    _max = max(_max, node[1])
            res = max(_max - _min + 1, res)
            
        return res