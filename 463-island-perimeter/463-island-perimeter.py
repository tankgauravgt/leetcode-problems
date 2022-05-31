class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        nR = len(grid)
        nC = len(grid[0])
        
        res = 0
        for ix in range(nR):
            for jx in range(nC):
                if grid[ix][jx] == 1:
                    res = res + 4
                    if ix > 0 and grid[ix - 1][jx] == 1:
                        res = res - 2
                    if jx > 0 and grid[ix][jx - 1] == 1:
                        res = res - 2
        return res