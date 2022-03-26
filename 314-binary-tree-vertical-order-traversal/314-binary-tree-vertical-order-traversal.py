# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.rec = {}
    
    def call(self, root, x, y):
        if root != None:
            if x in self.rec.keys():
                self.rec[x] = self.rec[x] + [(root.val, y)]
            else:
                self.rec[x] = [(root.val, y)]
            self.call(root.left, x-1, y+1)
            self.call(root.right, x+1, y+1)
    
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.call(root, 0, 0)
        
        out = []
        for k in sorted(self.rec.keys()):
            self.rec[k].sort(key=lambda x: x[1])
            out += [list(map(lambda x: x[0], self.rec[k]))]
            
        return out