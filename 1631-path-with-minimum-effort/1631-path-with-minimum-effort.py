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
        
        G = {ix: [] for ix in range(nR * nC)}
        for rx in range(nR):
            for cx in range(nC):
                for adj, weight in get_neighbors(rx, cx):
                    G[nC * rx + cx].append((nC * adj[0] + adj[1], weight))
        
        distances = [float('inf')] * (nR * nC)
        distances[0] = 0
        hq = [(0, 0)]
        
        while hq:
            dist, curr = heapq.heappop(hq)
            if curr == nR * nC - 1:
                return distances[curr]
            if distances[curr] < dist:
                continue
            for adj, weight in G[curr]:
                if distances[adj] <= max(distances[curr], weight):
                    continue
                distances[adj] = max(distances[curr], weight)
                heapq.heappush(hq, (distances[adj], adj))
        
        return float('inf')