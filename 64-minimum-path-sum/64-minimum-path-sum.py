class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        for ix in range(nR - 1):
            grid[ix + 1][0] = grid[ix][0] + grid[ix + 1][0]

        for jx in range(nC - 1):
            grid[0][jx + 1] = grid[0][jx] + grid[0][jx + 1]
        
        for ix in range(1, nR, 1):
            for jx in range(1, nC, 1):
                grid[ix][jx] = min(grid[ix - 1][jx], grid[ix][jx - 1]) + grid[ix][jx]
        
        return grid[nR - 1][nC - 1]