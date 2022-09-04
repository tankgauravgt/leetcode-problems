from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return None
        
        fringe = deque([node])
        clones = {node.val: Node(node.val, [])}
        
        while fringe:
            N = len(fringe)
            for ix in range(N):
                temp = fringe.popleft()
                curr = clones[temp.val]
                for adj in temp.neighbors:
                    if adj.val not in clones:
                        clones[adj.val] = Node(adj.val, [])
                        fringe.append(adj)
                    curr.neighbors.append(clones[adj.val])
        
        return clones[node.val]