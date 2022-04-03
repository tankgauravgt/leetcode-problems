from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.data = []

    def recurse(self, root, x, y):
        if root:
            self.recurse(root.left, x - 1, y + 1)
            self.data += [(root.val, x, y)]
            self.recurse(root.right, x + 1, y + 1)
        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        self.recurse(root, 0, 0)
        self.data.sort(key=lambda x: x[2])
        
        mx = max(map(lambda x: x[2], self.data))
        
        res = []
        for ix in range(mx + 1):
            if ix % 2 == 0:
                tmp = list(filter(lambda x: x[2] == ix, self.data))
                res += [map(lambda x: x[0], tmp)]
            else:
                tmp = list(filter(lambda x: x[2] == ix, self.data))[::-1]
                res += [map(lambda x: x[0], tmp)]
            
        return res