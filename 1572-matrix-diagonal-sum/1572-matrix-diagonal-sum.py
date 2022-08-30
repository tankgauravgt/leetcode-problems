class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        
        totalSum = 0
        if n % 2:
            for ix in range(n // 2):
                totalSum += mat[ix][ix]
                totalSum += mat[n - ix - 1][n - ix - 1]
            for ix in range(n):
                totalSum += mat[n - ix - 1][ix]
        else:
            for ix in range(n):
                totalSum += mat[ix][ix]
            for ix in range(n):
                totalSum += mat[n - ix - 1][ix]
        
        return totalSum