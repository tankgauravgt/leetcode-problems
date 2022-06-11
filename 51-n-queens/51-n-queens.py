class Solution:        
    
    def backtrack(self, row, N):
        if row == N:
            self.result.append(["".join(rarr) for rarr in self.mat])
        for cx in range(N):
            if not self.clash(row, cx, N):
                self.mat[row][cx] = 'Q'
                self.backtrack(row + 1, N)
                self.mat[row][cx] = '.'
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        out = []
        mat = [['.'] * n for ix in range(n)]        
        
        
        # =======================================
        # check for clash if any:
        # =======================================
        
        def clash(row, col, N):
            # check for column clash:
            vc = 0
            for rx in range(row):
                if mat[rx][col] == 'Q':
                    return True

            # check for left diagonal clash:
            ix = row
            jx = col
            while ix >= 0 and jx >= 0:
                if mat[ix][jx] == 'Q':
                    return True
                ix = ix - 1
                jx = jx - 1

            # check for right diagonal clash:
            ix = row
            jx = col
            while ix >= 0 and jx < N:
                if mat[ix][jx] == 'Q':
                    return True
                ix = ix - 1
                jx = jx + 1
            
            return False

        
        # ========================================
        # backtrack and find solution:
        # ========================================
        
        def backtrack(row, N):
            if row == N:
                out.append(["".join(rarr) for rarr in mat])
            for cx in range(N):
                if not clash(row, cx, N):
                    mat[row][cx] = 'Q'
                    backtrack(row + 1, N)
                    mat[row][cx] = '.'
        
        # call solveNQueens:
        backtrack(0, n)
        
        return out