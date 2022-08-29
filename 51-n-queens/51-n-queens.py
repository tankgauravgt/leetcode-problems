class Solution:        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def valid(rx, cx):
            for r in range(0, rx):
                if grid[r][cx] == "Q":
                    return False
            r, c = rx, cx
            while r >= 0 and c >= 0:
                if grid[r][c] == "Q":
                    return False
                r = r - 1
                c = c - 1
            
            r, c = rx, cx
            while r < nR and c < nC:
                if grid[r][c] == "Q":
                    return False
                r = r - 1
                c = c + 1
            return True
        
        
        nR = nC = n
        grid = [["."] * nC for _ in range(nR)]
        
        res = []
        def solve(rx):
            nonlocal grid
            if rx == nR:
                res.append(["".join(row) for row in grid])
                return
            for c in range(nC):
                if valid(rx, c):
                    grid[rx][c] = "Q"
                    solve(1 + rx)
                    grid[rx][c] = "."
        
        solve(0)
        return res