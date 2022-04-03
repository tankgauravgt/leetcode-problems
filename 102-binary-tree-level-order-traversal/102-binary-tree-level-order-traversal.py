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
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        self.recurse(root, 0, 0)
        self.data.sort(key=lambda x: x[2])
        
        depth = max(map(lambda x: x[2], self.data))
        
        res = []
        for d in range(1 + depth):
            temp = list(filter(lambda x: x[2] == d, self.data))
            res += [list(map(lambda x: x[0], temp))]
        
        return res