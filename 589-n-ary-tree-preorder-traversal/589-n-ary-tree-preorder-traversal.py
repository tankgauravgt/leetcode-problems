"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def preorder(node):
            nonlocal out
            if node:
                out.append(node.val)
                for child in node.children:
                    preorder(child)
        
        out = []
        preorder(root)
        
        return out