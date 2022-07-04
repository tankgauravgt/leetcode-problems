class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(rx, cx):
            nonlocal grid, count
            grid[rx][cx] = 0
            count = count + 1
            if rx < len(grid) - 1 and grid[rx + 1][cx] == 1:
                dfs(rx + 1, cx)
            if cx < len(grid[0]) - 1 and grid[rx][cx + 1] == 1:
                dfs(rx, cx + 1)
            if rx > 0 and grid[rx - 1][cx] == 1:
                dfs(rx - 1, cx)
            if cx > 0 and grid[rx][cx - 1] == 1:
                dfs(rx, cx - 1)
        
        count = 0
        max_area = 0
        for ix in range(len(grid)):
            for jx in range(len(grid[0])):
                if grid[ix][jx] == 1:
                    count = 0
                    dfs(ix, jx)
                    max_area = max(count, max_area)
        
        return max_area