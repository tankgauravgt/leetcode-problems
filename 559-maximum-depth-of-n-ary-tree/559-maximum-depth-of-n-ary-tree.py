"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node):
            if node:
                depths = []
                for child in node.children:
                    depths.append(dfs(child))
                if depths:
                    return 1 + max(depths)
                return 1
            return 0
        
        return dfs(root)