class Solution:
    
    def clash(self, row, col, N):
        
        vc = 0
        for rx in range(row):
            if self.mat[rx][col] == 'Q':
                return True
        
        ix = row
        jx = col
        while ix >= 0 and jx >= 0:
            if self.mat[ix][jx] == 'Q':
                return True
            ix = ix - 1
            jx = jx - 1
        
        ix = row
        jx = col
        while ix >= 0 and jx < N:
            if self.mat[ix][jx] == 'Q':
                return True
            ix = ix - 1
            jx = jx + 1
        
        return False
        
    
    def backtrack(self, row, N):
        if row == N:
            self.result += [["".join(rarr) for rarr in self.mat]]
        for cx in range(N):
            if not self.clash(row, cx, N):
                self.mat[row][cx] = 'Q'
                self.backtrack(row + 1, N)
                self.mat[row][cx] = '.'
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # create board:
        self.mat = [['.'] * n for ix in range(n)]
        
        # create result:
        self.result = []
        
        # call solveNQueens:
        self.backtrack(0, n)
        
        return self.result