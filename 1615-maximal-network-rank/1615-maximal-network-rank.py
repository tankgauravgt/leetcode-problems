class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        D = {ix: 0 for ix in range(n)}
        
        for u, v in roads:
            D[u] += 1
            D[v] += 1
            
        maxrank = 0
        rec = set(list(map(lambda x: tuple(x), roads)))
        for ix in range(n):
            for jx in range(1 + ix, n):
                if (ix, jx) in rec or (jx, ix) in rec:
                    maxrank = max(maxrank, D[ix] + D[jx] - 1)
                else:
                    maxrank = max(maxrank, D[ix] + D[jx])
        return maxrank