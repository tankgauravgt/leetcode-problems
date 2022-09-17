class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        nR = len(heights)
        nC = len(heights[0])
        
        def adjs(r, c):
            buf = []
            for rx, cx in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if rx in range(0, nR) and cx in range(0, nC) and heights[rx][cx] >= heights[r][c]:
                    buf.append((rx, cx))
            return buf
        
        def bfs(dq):
            vrec = set(dq)
            while dq:
                rr, cc = dq.popleft()
                for adj in adjs(rr, cc):
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            return vrec
        
        pacific = deque()
        for rx in range(1, nR):
            pacific.append((rx, 0))
        for cx in range(0, nC):
            pacific.append((0, cx))
        
        atlantic = deque()
        for rx in range(0, nR - 1):
            atlantic.append((rx, nC - 1))
        for cx in range(0, nC):
            atlantic.append((nR - 1, cx))
        
        s1 = bfs(pacific)
        s2 = bfs(atlantic)
        
        return s1.intersection(s2)