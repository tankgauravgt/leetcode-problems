class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # store result here:
        res = 0
        
        # create board:
        grid = []
        for ix in range(n):
            grid.append([0] * n)

        # check if king position possible:
        def clash(rx, cx):
            nonlocal n, grid
            
            # check on column:
            for ix in range(rx):
                if grid[ix][cx] == 1:
                    return True
            
            # check left top diag:
            rr, cc = rx, cx
            while rr >= 0 and cc >= 0:
                if grid[rr][cc] == 1:
                    return True
                rr = rr - 1
                cc = cc - 1
                
            # check right top diag:
            rr, cc = rx, cx
            while rr >= 0 and cc < n:
                if grid[rr][cc] == 1:
                    return True
                rr = rr - 1
                cc = cc + 1
            
            # return False: (default)
            return False
        
        def recurse(row):
            nonlocal n, res, grid
            if row == n:
                res = res + 1
                return
            for cx in range(n):
                if not clash(row, cx):
                    grid[row][cx] = 1
                    recurse(row + 1)
                    grid[row][cx] = 0
        
        # calculate possibilities:
        recurse(0)
        
        # return answer:
        return res