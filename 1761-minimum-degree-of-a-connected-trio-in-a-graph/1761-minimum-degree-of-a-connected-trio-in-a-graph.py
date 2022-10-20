class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        D = {ix: 0 for ix in range(1, 1 + n)}
        G = {ix: set() for ix in range(1, 1 + n)}
        
        rec = set()
        for u, v in edges:
            D[u] = D[u] + 1
            D[v] = D[v] + 1
            G[u].add(v)
            G[v].add(u)
            if u > v:
                rec.add((v, u))
            else:
                rec.add((u, v))                
        
        minval = float('inf')
        for ix in range(1, 1 + n):
            for jx in range(1 + ix, 1 + n):
                if (ix, jx) in rec:
                    common = G[ix] & G[jx]
                    for kx in filter(lambda x: x > jx, common):
                        if ix in G[kx] and jx in G[kx]:
                            minval = min(minval, D[ix] + D[jx] + D[kx] - 6)
        
        return -1 if minval == float('inf') else minval