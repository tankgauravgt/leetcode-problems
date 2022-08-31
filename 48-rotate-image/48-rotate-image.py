class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for ix in range(len(matrix)):
            for jx in range(1 + ix, len(matrix[0])):
                matrix[ix][jx], matrix[jx][ix] = matrix[jx][ix], matrix[ix][jx]
        
        for rx, row in enumerate(matrix):
            matrix[rx] = row[::-1]