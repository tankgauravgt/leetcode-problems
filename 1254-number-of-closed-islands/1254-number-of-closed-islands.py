class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        def dfs(rx, cx):
            nonlocal grid, nR, nC, valid
            if rx == 0 or cx == 0 or rx == (nR - 1) or cx == (nC - 1):
                valid = False
            grid[rx][cx] = 1
            if cx < (nC - 1) and grid[rx][cx + 1] == 0:
                dfs(rx, cx + 1)
            if cx > 0 and grid[rx][cx - 1] == 0:
                dfs(rx, cx - 1)
            if rx < (nR - 1) and grid[rx + 1][cx] == 0:
                dfs(rx + 1, cx)
            if rx > 0 and grid[rx - 1][cx] == 0:
                dfs(rx - 1, cx)
        
        count = 0
        for ix in range(nR):
            for jx in range(nC):
                if grid[ix][jx] == 0:
                    valid = True
                    dfs(ix, jx)
                    if valid:
                        count += 1
        
        return count