class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        total = 0
        for row in grid:
            total = total + sum(row)
        
        if total == 0 or total == nR * nC:
            return -1
        
        ctr = 0
        dq = deque([(rx, cx) for rx in range(nR) for cx in range(nC) if grid[rx][cx] == 1])
        vrec = set([(rx, cx) for rx in range(nR) for cx in range(nC) if grid[rx][cx] == 1])
        
        while dq:
            N = len(dq)
            for ix in range(N):
                r, c = dq.popleft()
                for adj in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
                    if adj[0] not in range(0, nR) or adj[1] not in range(0, nC):
                        continue
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            ctr = ctr + 1
        
        return ctr - 1