class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(rx, cx):
            nonlocal grid, valid, count
            if (rx == 0) or (cx == 0) or (rx == len(grid) - 1) or (cx == len(grid[0]) - 1):
                valid = False
            count = count + 1
            grid[rx][cx] = 0
            if rx > 0 and grid[rx - 1][cx] == 1:
                dfs(rx - 1, cx)
            if rx < len(grid) - 1 and grid[rx + 1][cx] == 1:
                dfs(rx + 1, cx)
            if cx > 0 and grid[rx][cx - 1] == 1:
                dfs(rx, cx - 1)
            if cx < len(grid[0]) - 1 and grid[rx][cx + 1] == 1:
                dfs(rx, cx + 1)
        
        total_count = 0
        for ix in range(len(grid)):
            for jx in range(len(grid[0])):
                if grid[ix][jx] == 1:
                    count = 0
                    valid = True
                    dfs(ix, jx)
                    if valid:
                        total_count += count
        return total_count