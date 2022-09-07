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
        
        if not node:
            return node
        
        G = {}
        vrec = set([node.val])
        
        dq = deque([node])
        while dq:
            temp = dq.popleft()
            if temp.val not in G:
                G[temp.val] = Node(temp.val, [])
            for adj in temp.neighbors:
                if adj.val not in G:
                    G[adj.val] = Node(adj.val, [])
                if adj.val not in vrec:
                    vrec.add(adj.val)
                    dq.append(adj)
                G[temp.val].neighbors.append(G[adj.val])
        
        return G[node.val]