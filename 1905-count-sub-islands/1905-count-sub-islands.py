class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        nR = len(grid2)
        nC = len(grid2[0])
        
        def dfs(rx, cx):
            nonlocal grid1, grid2, nR, nC, valid
            if grid1[rx][cx] == 0:
                valid = False
            grid2[rx][cx] = 0
            if rx > 0 and grid2[rx - 1][cx] == 1:
                dfs(rx - 1, cx)
            if cx > 0 and grid2[rx][cx - 1] == 1:
                dfs(rx, cx - 1)
            if rx < (nR - 1) and grid2[rx + 1][cx] == 1:
                dfs(rx + 1, cx)
            if cx < (nC - 1) and grid2[rx][cx + 1] == 1:
                dfs(rx, cx + 1)
        
        count = 0
        for ix in range(nR):
            for jx in range(nC):
                valid = True
                if grid2[ix][jx] == 1:
                    dfs(ix, jx)
                    if valid == True:
                        count += 1
        return count