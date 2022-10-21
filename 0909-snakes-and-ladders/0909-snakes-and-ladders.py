from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        
        seq = []
        for ix, arr in enumerate(board[::-1]):
            seq.extend(arr[::-1] if ix % 2 else arr[::1])
        
        for ix in range(n * n):
            if seq[ix] == -1:
                seq[ix] = 1 + ix
            seq[ix] = seq[ix] - 1
        
        dq = deque([0])
        vrec = set([0])
        
        ctr = 0
        while dq:
            N = len(dq)
            for ix in range(N):
                curr = dq.popleft()
                if curr == (n * n) - 1:
                    return ctr
                for dx in range(1, 7):
                    adj = seq[min(curr + dx, n * n - 1)]
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            ctr = ctr + 1
        
        return -1
