class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        out_mat = [[0] * len(matrix) for ix in range(len(matrix[0]))]
        for ix in range(len(matrix)):
            for jx in range(len(matrix[0])):
                out_mat[jx][ix] = matrix[ix][jx]
        return out_mat