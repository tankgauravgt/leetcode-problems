# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.deepest = 0
        self.result = []
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root != None:
            self.result += [root.val]
            self.recursive_probe(root, 0)
        
        return self.result
    
    
    def recursive_probe(self, node, d):
        
        if d > self.deepest:
            self.deepest = d
            self.result += [node.val]
        
        if node.right != None:
            self.recursive_probe(node.right, d + 1)
        if node.left != None:
            self.recursive_probe(node.left, d + 1)