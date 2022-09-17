from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        nR = len(grid)
        nC = len(grid[0])
        
        def adjs(r, c):
            buf = []
            for rx, cx in [(r, c + 1), (r - 1, c + 1),
                           (r - 1, c), (r - 1, c - 1), 
                           (r, c - 1), (r + 1, c - 1), 
                           (r + 1, c), (r + 1, c + 1)
                          ]:
                if rx in range(0, nR) and cx in range(0, nC):
                    if grid[rx][cx] == 0:
                        buf.append((rx, cx))
            return buf
        
        dq = deque([(0, 0)])
        vrec = set([(0, 0)])
        
        ctr = 0
        while dq:
            N = len(dq)
            for ix in range(N):
                rr, cc = dq.popleft()
                if rr == (nR - 1) and cc == (nC - 1):
                    return 1 + ctr
                for adj in adjs(rr, cc):
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            ctr = ctr + 1
            
        return -1