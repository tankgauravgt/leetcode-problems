class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nR = len(grid)
        nC = len(grid[0])
        
        tab = [[0] * nC for jx in range(nR)]
        
        tab[0][0] = grid[0][0]
        
        for ix in range(nR - 1):
            tab[ix + 1][0] = tab[ix][0] + grid[ix + 1][0]

        for jx in range(nC - 1):
            tab[0][jx + 1] = tab[0][jx] + grid[0][jx + 1]
        
        for ix in range(1, nR, 1):
            for jx in range(1, nC, 1):
                tab[ix][jx] = min(tab[ix - 1][jx], tab[ix][jx - 1]) + grid[ix][jx]
        
        print(tab)        
        return tab[nR - 1][nC - 1]