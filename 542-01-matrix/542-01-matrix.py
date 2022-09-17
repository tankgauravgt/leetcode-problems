class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        nR = len(mat)
        nC = len(mat[0])
        
        def adjs(r, c):
            buf = []
            for rx, cx in [(r, c + 1), (r + 1, c), (r - 1, c), (r, c - 1)]:
                if rx in range(0, nR) and cx in range(0, nC):
                    buf.append((rx, cx))
            return buf
        
        vrec = set([(rx, cx) for rx in range(nR) for cx in range(nC) if mat[rx][cx] == 0])
        dq = deque([(rx, cx) for rx in range(nR) for cx in range(nC) if mat[rx][cx] == 0])

        ctr = 0
        while dq:
            N = len(dq)
            for ix in range(N):
                rr, cc = dq.popleft()
                if mat[rr][cc] == 1:
                    mat[rr][cc] = ctr
                for adj in adjs(rr, cc):
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            ctr = ctr + 1
        return mat