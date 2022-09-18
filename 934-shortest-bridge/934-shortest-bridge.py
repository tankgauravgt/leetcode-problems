from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        sr, sc = -1, -1
        for ix in range(nR):
            for jx in range(nC):
                if grid[ix][jx] == 1:
                    sr, sc = ix, jx
                    
        dq = deque([(sr, sc)])
        vrec = set(dq)
        while dq:
            rr, cc = dq.popleft()
            for r, c in [(rr, cc + 1), (rr, cc - 1), (rr + 1, cc), (rr - 1, cc)]:
                if r in range(0, nR) and c in range(0, nC):
                    if grid[r][c] == 1 and (r, c) not in vrec:
                        vrec.add((r, c))
                        dq.append((r, c))
        
        dq = deque(vrec)
        cnt = 0
        while dq:
            N = len(dq)
            for ix in range(N):
                rr, cc = dq.popleft()
                if cnt != 0 and grid[rr][cc] == 1:
                    return cnt - 1
                for r, c in [(rr, cc + 1), (rr, cc - 1), (rr + 1, cc), (rr - 1, cc)]:
                    if r in range(0, nR) and c in range(0, nC):
                        if (r, c) not in vrec:
                            vrec.add((r, c))
                            dq.append((r, c))
            cnt = cnt + 1
        
        return cnt - 1