import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        nR = len(heights)
        nC = len(heights[0])
        
        def get_neighbors(rx, cx):
            adjs = []
            for dr, dc in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
                if rx + dr in range(nR) and cx + dc in range(nC):
                    diff = abs(heights[rx + dr][cx + dc] - heights[rx][cx])
                    adjs.append(((rx + dr, cx + dc), diff))
            return adjs
        
        elist = []
        for rx in range(nR):
            for cx in range(nC):
                src = nC * rx + cx
                for adj, weight in get_neighbors(rx, cx):
                    dest = nC * adj[0] + adj[1]
                    elist.append((weight, src, dest))
        elist.sort(reverse=True)
        
        dset = {}
        def find(rec, x):
            rec[x] = y = rec.get(x, x)
            if y != x:
                rec[x] = y = find(rec, y)
            return y
        
        def union(rec, x, y):
            rec[find(rec, y)] = find(rec, x)
        
        while elist:
            w, s, d = elist.pop()
            union(dset, s, d)
            if find(dset, 0) == find(dset, nC * nR - 1):
                return w
        
        return 0