from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        def adjs(r, c):
            drdc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            buf = []
            for dr, dc in drdc:
                if (r + dr) in range(0, nR) and (c + dc) in range(0, nC):
                    if grid[r + dr][c + dc] == 1:
                        buf.append((r + dr, c + dc))
            return buf
        
        
        vrec = set()
        def bfs(sr, sc):
            
            if (sr, sc) in vrec:
                return (False, 0)
            
            ctr = 0
            valid = True
            vrec.add((sr, sc))
            dq = deque([(sr, sc)])
            while dq:
                rr, cc = dq.popleft()
                ctr = ctr + 1
                if rr == 0 or rr == (nR - 1) or cc == 0 or cc == (nC - 1):
                    valid = False
                for adj in adjs(rr, cc):
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            return (valid, ctr)
        
        total = 0
        for ix in range(1, nR):
            for jx in range(1, nC):
                if grid[ix][jx] == 1:
                    res = bfs(ix, jx)
                    total = total + (res[1] if res[0] else 0)
        return total