class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        G = {}
        for u, v in edges:
            G[u] = 1 + G.get(u, 0)
            G[v] = 1 + G.get(v, 0)
        
        for k, v in G.items():
            if v != 1:
                return k
        return None