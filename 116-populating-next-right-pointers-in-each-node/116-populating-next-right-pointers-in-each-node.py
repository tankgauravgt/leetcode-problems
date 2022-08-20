from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        fringe = deque([root])
        
        while fringe:
            
            N = len(fringe)
            fx = fringe.popleft()
            if fx:
                fringe.append(fx.left)
                fringe.append(fx.right)
                for ix in range(N - 1):
                    sx = fringe.popleft()
                    if sx:
                        fringe.append(sx.left)
                        fringe.append(sx.right)
                    fx.next = sx
                    fx = sx
                fx.next = None
        
        return root