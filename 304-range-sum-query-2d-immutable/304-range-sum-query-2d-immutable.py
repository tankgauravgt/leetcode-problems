class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        nR = len(matrix)
        nC = len(matrix[0])
        
        self.mat = [[0] * (1 + nC) for ix in range(1 + nR)]
        
        for ix in range(1, 1 + nR):
            for jx in range(1, 1 + nC):
                self.mat[ix][jx] = matrix[ix - 1][jx - 1]
        
        for ix in range(1, 1 + nR):
            for jx in range(1, 1 + nC):
                self.mat[ix][jx] += (self.mat[ix - 1][jx] + self.mat[ix][jx - 1] - self.mat[ix - 1][jx - 1])
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        fsum = self.mat[1 + row2][1 + col2]
        tmat = self.mat[row1][1 + col2]
        smat = self.mat[1 + row2][col1]
        cmat = self.mat[row1][col1]
        return fsum - tmat - smat + cmat
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)