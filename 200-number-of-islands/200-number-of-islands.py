class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if (r+1) < R and grid[r+1][c] == "1":
                    dfs(r+1, c)
                if 0 <= (r-1) and grid[r-1][c] == "1":
                    dfs(r-1, c)
                if (c+1) < C and grid[r][c+1] == "1":
                    dfs(r, c+1)
                if 0 <= (c-1) and grid[r][c-1] == "1":
                    dfs(r, c-1)
            else:
                return
        
        ctr = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                        dfs(r, c)
                        ctr += 1
        
        return ctr